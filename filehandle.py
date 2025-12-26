# file_handling.py

# Step 1: Write to a file (this will create the file if it doesn't exist)
with open("example.txt", "w") as file:
    file.write("Hello, this is the first line.\n")
    file.write("Python file handling example.\n")

# Step 2: Append data to the same file
with open("example.txt", "a") as file:
    file.write("This line is appended later.\n")

# Step 3: Read the file content
with open("example.txt", "r") as file:
    content = file.read()

# Step 4: Display file content
print("File Content:")
print(content)
