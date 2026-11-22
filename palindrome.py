number = int(input("Enter a number: "))

original_number = number
reversed_number = 0

while number > 0:
    digit = number % 10
    reversed_number = reversed_number * 10 + digit
    number = number // 10

if original_number == reversed_number:
    print("Palindrome Number")
else:
    print("Not a Palindrome Number")