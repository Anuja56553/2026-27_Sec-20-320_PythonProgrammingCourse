total_rows = int(input("Enter number of rows: "))

number = 1

for row in range(1, total_rows + 1):

    for column in range(row):
        print(number, end=" ")
        number = number + 1

    print()