#Conditions
score = int(input("Enter your marks"))

#If, else & elif
if score > 100:
    print("Wrong entry")
elif score >=90:
    print("Grade S Distinction")
elif score >= 80:
    print("Grade A Excellent")
elif score >=70:
    print("Grade B Good")
elif score >=50:
    print("C You are Passed")
else:
    print("Failed")

#nested If

age = int(input("enter your age"))

pro = input("Enter your plan")

if age >=18 :
    if pro:
        print("You pro user full access available")
    else:
        print("Limited access available")
else:
    print("You are in base plan")

#ternary condition
status = "Adult" if age >=18 else "Minor"
print(status)

