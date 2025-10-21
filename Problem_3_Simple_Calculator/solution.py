# your code here
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

operation = input("Choose operation (+, -, *, /): ").strip()
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operation == '+':
    print(add(num1, num2))
elif operation == '-':
    print(subtract(num1, num2))
elif operation == '*':
    print(multiply(num1, num2))
elif operation == '/':
    if num2 != 0:
        print(divide(num1, num2))
    else:
        print("Error: Division by zero")
else:
    print("Invalid operation")

