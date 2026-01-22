# =====================================================
# STUDENT RESULT MANAGEMENT SYSTEM
# Demonstrates:
# Variables, Operators, Conditions, Loops
# =====================================================

print("====== STUDENT RESULT MANAGEMENT SYSTEM ======\n")

# -------------------------------
# VARIABLES
# -------------------------------

maths = int(input("enter the marks"))
science = int(input("enter the marks"))
english = int(input("enter the marks"))

print("\n")
student_name = "Arul Kumar"
student_id = 101

print("Student Name:", student_name)
print("Student ID:", student_id)

# -------------------------------
# OPERATORS (Arithmetic)
# -------------------------------
total_marks = maths + science + english
average_marks = total_marks / 3

print("\nTotal Marks:", total_marks)
print("Average Marks:", average_marks)

# -------------------------------
# CONDITIONS (if-elif-else)
# -------------------------------
if average_marks >= 90:
    grade = "A+"
elif average_marks >= 75:
    grade = "A"
elif average_marks >= 60:
    grade = "B"
else:
    grade = "C"

print("Grade:", grade)

# -------------------------------
# LOGICAL OPERATORS
# -------------------------------
is_pass = maths >= 35 and science >= 35 and english >= 35

if is_pass:
    result = "PASS"
else:
    result = "FAIL"

print("Result:", result)

# -------------------------------
# TERNARY OPERATOR
# -------------------------------
scholarship = "Eligible" if average_marks >= 80 else "Not Eligible"
print("Scholarship:", scholarship)

# -------------------------------
# LOOP (for)
# -------------------------------
print("\nSubject-wise Marks:")

subjects = ["Maths", "Science", "English"]
marks = [maths, science, english]

for i in range(len(subjects)):
    print(subjects[i], ":", marks[i])

# -------------------------------
# LOOP (while)
# -------------------------------
print("\nChecking marks validation...")

i = 0
while i < len(marks):
    if marks[i] < 0 or marks[i] > 100:
        print("Invalid marks detected!")
        break
    i += 1
else:
    print("All marks are valid")

# -------------------------------
# NESTED CONDITIONS
# -------------------------------
print("\nPerformance Review:")

if result == "PASS":
    if average_marks >= 80:
        print("Excellent Performance")
    elif average_marks >= 65:
        print("Good Performance")
    else:
        print("Needs Improvement")
else:
    print("Must repeat the exam")

print("\n====== END OF PROGRAM ======")
