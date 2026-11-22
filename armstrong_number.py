number = int(input("Enter a three-digit number: "))

original_number = number
armstrong_sum = 0

while number > 0:
    digit = number % 10
    armstrong_sum = armstrong_sum + digit ** 3
    number = number // 10

if armstrong_sum == original_number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")