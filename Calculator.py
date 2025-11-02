#Thomas Anstis
#02/11/2025
#Calculator

operator = input("Enter an operator (+ - * /) ")
num1 = float(input("Enter the first number "))
num2 = float(input("Enter the second number "))

if operator == "+":
    result = num1 + num2
    print(round(result, 2))
elif operator == "-":
    result = num1 - num2
    print(round(result, 2))
elif operator == "*":
    result = num1 * num2
    print(round(result, 2))
elif operator == "/":
    result = num1 / num2
    print(round(result, 2))
else:
    print(f"{operator} is INVALID!")

#Arithmetic Calculator (Python)
#Built a console-based calculator that performs basic arithmetic operations (+, –, *, /) based on user input.
#Demonstrated proficiency in Python fundamentals including data types, conditional logic, type casting, and user input handling.
#Designed with clean output formatting and error messaging for improved user experience.
