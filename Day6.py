#Dictionary 
'''
profile = {"name" : "Arul" , "location" : "bangalore"}
print(profile)
'''

name = str(input("enter Name"))
city = str(input("enter City"))

# Dictionary 1: Employee personal details
employee_personal = {
    "emp_id": 101,
    "name": name,
    "city": city
}

desig = str(input("enter designation"))
dept = str(input("enter department"))
exper = int(input("enter Experience"))

# Dictionary 2: Employee job details
employee_job = {
    "designation": desig,
    "department": dept,
    "experience": exper
}
base = 200000
salary = exper * base

# Dictionary 3: Employee salary details
employee_salary = {
    "salary": salary,
    "currency": "INR"
}

# ---- Merge all dictionaries ----
employee_profile = {}

employee_profile.update(employee_personal)
employee_profile.update(employee_job)
employee_profile.update(employee_salary)

# Print merged dictionary
print("Merged Employee Profile:\n")

for key, value in employee_profile.items():
    print(key, ":", value)
