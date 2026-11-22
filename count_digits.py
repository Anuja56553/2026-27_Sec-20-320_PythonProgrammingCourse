number = int(input("Enter a number: "))

number = abs(number)
digit_count = 0

if number == 0:
    digit_count = 1
else:
    while number > 0:
        digit_count = digit_count + 1
        number = number // 10

print("Number of digits =", digit_count)