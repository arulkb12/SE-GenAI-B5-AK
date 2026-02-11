import os
import json
import tempfile
from dotenv import load_dotenv
from neo4j import GraphDatabase

from langchain_openai import ChatOpenAI
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# -----------------------------
# LLM & DB
# -----------------------------
llm = ChatOpenAI(
    model="gpt-5-nano",
    temperature=0
)

driver = GraphDatabase.driver(
    os.getenv("NEO4J_URI"),
    auth=(os.getenv("NEO4J_USERNAME"), os.getenv("NEO4J_PASSWORD"))
)

# -----------------------------
# Text Splitter (CRITICAL FIX)
# -----------------------------
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1500,     # SAFE for GPT-3.5
    chunk_overlap=200
)

# -----------------------------
# Extract KG from ONE CHUNK
# -----------------------------
def extract_kg(chunk_text: str):
    prompt = ChatPromptTemplate.from_template(
        """
Extract Program Management knowledge as JSON.
Return STRICT JSON only.

Schema:
{{
  "programs": [
    {{
      "name": "string",
      "milestones": ["string"],
      "risks": ["string"],
      "owner": "string"
    }}
  ]
}}

Text:
{text}
"""
    )

    response = (prompt | llm).invoke({"text": chunk_text})

    try:
        return json.loads(response.content)
    except json.JSONDecodeError:
        return {"programs": []}   # safe fallback

# -----------------------------
# Store KG in Neo4j
# -----------------------------
def store_kg(data):
    with driver.session() as session:
        for p in data.get("programs", []):

            session.run(
                """
                MERGE (pr:Program {name:$name})
                MERGE (o:Owner {name:$owner})
                MERGE (pr)-[:OWNED_BY]->(o)
                """,
                name=p.get("name"),
                owner=p.get("owner", "Unknown")
            )

            for m in p.get("milestones", []):
                session.run(
                    """
                    MERGE (m:Milestone {name:$milestone})
                    MERGE (pr:Program {name:$program})
                    MERGE (pr)-[:HAS_MILESTONE]->(m)
                    """,
                    milestone=m,
                    program=p.get("name")
                )

            for r in p.get("risks", []):
                session.run(
                    """
                    MERGE (r:Risk {name:$risk})
                    MERGE (pr:Program {name:$program})
                    MERGE (pr)-[:HAS_RISK]->(r)
                    """,
                    risk=r,
                    program=p.get("name")
                )

# -----------------------------
# Build KG (TOKEN-SAFE)
# -----------------------------
def build_kg(uploaded_files):
    with tempfile.TemporaryDirectory() as tmp:
        for file in uploaded_files:
            path = os.path.join(tmp, file.name)

            with open(path, "wb") as f:
                f.write(file.getbuffer())

            pages = PyPDFLoader(path).load()
            full_text = "\n".join(p.page_content for p in pages)

            chunks = splitter.split_text(full_text)

            for chunk in chunks:
                kg_data = extract_kg(chunk)
                store_kg(kg_data)

# -----------------------------
# KG Question Answering
# -----------------------------
def query_kg(question: str):
    cypher_prompt = ChatPromptTemplate.from_template(
        """
Convert the question into a Cypher query.
Return ONLY Cypher.

Schema:
(:Program)-[:HAS_MILESTONE]->(:Milestone)
(:Program)-[:HAS_RISK]->(:Risk)
(:Program)-[:OWNED_BY]->(:Owner)

Question:
{question}
"""
    )

    cypher = (cypher_prompt | llm).invoke(
        {"question": question}
    ).content.strip()

    with driver.session() as session:
        result = session.run(cypher)
        records = [dict(r) for r in result]

    answer_prompt = ChatPromptTemplate.from_template(
        """
Answer using only the graph results.

Graph Results:
{data}

Question:
{question}
"""
    )

    answer = (answer_prompt | llm).invoke(
        {"data": records, "question": question}
    ).content

    return answer