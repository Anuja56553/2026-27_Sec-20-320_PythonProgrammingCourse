#for loop
table_number = int(input("Enter a number: "))
for multiplier in range(1, 11):
    print(table_number, "x", multiplier, "=", table_number * multiplier)

#while loop
multiplier = 1
while multiplier <= 10:
    print(table_number, "x", multiplier, "=", table_number * multiplier)
    multiplier = multiplier + 1
