print("*********Calculator**********")

def calculator(a, b):
    print("\nCalculation Results\n")

    print("Addition:", a + b)
    print("Subtraction:", a - b)
    print("Multiplication:", a * b)

    if b != 0:
        print("Division:", a / b)
        print("Floor Division:", a // b)
        print("Modulus:", a % b)
    else:
        print("Division: Cannot divide by zero")

    print("Exponentiation:", a ** b)


# ---- Function Call ----
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

calculator(num1, num2)
