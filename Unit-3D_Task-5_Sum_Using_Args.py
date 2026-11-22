def find_sum(*args):
    total = 0
    for num in args:
        total = total + num
    return total

n = int(input("Enter how many numbers: "))

numbers = []

for i in range(n):
    num = int(input("Enter number: "))
    numbers.append(num)

result = find_sum(*numbers)

print("Sum =", result)