import streamlit as st
from kg_pipeline import build_kg, query_kg

st.set_page_config(page_title="PM Knowledge Graph Assistant")

st.title("🧠 Program Manager Knowledge Graph Assistant")

uploaded_files = st.file_uploader(
    "Upload Program documents (PDF)",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:
    with st.spinner("Building Knowledge Graph..."):
        build_kg(uploaded_files)
    st.success("Knowledge Graph updated successfully!")

question = st.text_input("Ask a Program Management question")

if question:
    with st.spinner("Querying Knowledge Graph..."):
        answer = query_kg(question)

    st.markdown("### Answer")
    st.write(answer)