table_number = int(input("Enter a number: "))

for multiplier in range(1, 11):
    product = table_number * multiplier
    print(table_number, "x", multiplier, "=", product)

table_number = int(input("Enter a number: "))

multiplier = 1

while multiplier <= 10:
    product = table_number * multiplier
    print(table_number, "x", multiplier, "=", product)
    multiplier = multiplier + 1