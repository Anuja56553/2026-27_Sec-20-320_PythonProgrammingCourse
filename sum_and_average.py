total_count = int(input("Enter how many numbers: "))

total_sum = 0

for count in range(1, total_count + 1):
    number = float(input("Enter a number: "))
    total_sum = total_sum + number

average = total_sum / total_count

print("Sum =", total_sum)
print("Average =", average)