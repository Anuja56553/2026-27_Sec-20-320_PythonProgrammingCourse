# Keyword and Positional Arguments

def divide(a, b):
    return a / b

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Keyword arguments
result1 = divide(b=second_number, a=first_number)
print("Division using keyword arguments:", result1)

# Positional arguments
result2 = divide(first_number, second_number)
print("Division using positional arguments:", result2)