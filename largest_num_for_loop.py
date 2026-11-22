#Largest Number in a Series Using for Loop
total_count = int(input("Enter how many numbers: "))

largest_number = float(input("Enter number 1: "))

for count in range(2, total_count + 1):
    number = float(input("Enter  number 2: "))

    if number > largest_number:
        largest_number = number

print("Largest number =", largest_number)