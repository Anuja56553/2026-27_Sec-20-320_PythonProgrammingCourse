# Prime Number Program

number = int(input("Enter a number (1 to 100): "))

if number <= 1:
    print("Not a Prime Number")
else:
    divisor = 2

    while divisor < number:
        if number % divisor == 0:
            break
        divisor = divisor + 1

    if divisor == number:
        print("Prime Number")
    else:
        print("Not a Prime Number")
