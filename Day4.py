#Loops 
'''
for i in range(0,10):
    print(i)

list = ['a', 'b', 6, 7]

for i in list:
    print(i)

'''

# Dictionary storing student names and their marks

Arul = int(input("enter Arul's marks"))
Rahul = int(input("enter Rahul's marks"))
Anita = int(input("enter Anita's marks"))

student_marks = {
    "Arul": Arul,
    "Rahul": Rahul,
    "Anita": Anita
}

print("\n Student Marks Report\n")

# for loop to iterate through dictionary
for student, marks in student_marks.items():
    print("Name:", student)
    print("Marks:", marks)

    if marks >= 80:
        print("Grade: A")
    elif marks >= 60:
        print("Grade: B")
    else:
        print("Grade: C")

    print("-" * 20)
