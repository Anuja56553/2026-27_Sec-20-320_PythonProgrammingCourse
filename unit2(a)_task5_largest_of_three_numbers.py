# Largest of Three Numbers Using Nested If

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))
third_number = int(input("Enter third number: "))

if first_number >= second_number:
    if first_number >= third_number:
        largest_number = first_number
    else:
        largest_number = third_number
else:
    if second_number >= third_number:
        largest_number = second_number
    else:
        largest_number = third_number

print("Largest Number =", largest_number)
