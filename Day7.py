skills = {"AI", "GIT HUB", "python", "AI"}

print(skills)

required = {"python", "DA"}

common = skills & required
print(common)

Or = skills | required
print(Or)

#frozen = frozenset(skills)
#print(frozen)

#**********Assignment***********

# Create a frozenset
allowed_roles = frozenset(["Admin", "Editor", "Viewer"])
user_role = str(input("Enter your role "))

print("Allowed Roles:\n")

# for loop to iterate over frozenset
for role in allowed_roles:
    print(role)

if user_role in allowed_roles:
    print("Access granted")
else:
    print("Access denied")
