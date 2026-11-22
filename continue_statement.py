#for loop
for number in range(1, 11):
    if number == 5:
        continue
    print(number)
    #while loop
    number = 1

while number <= 10:
    if number == 5:
        number = number + 1
        continue

    print(number)
    number = number + 1