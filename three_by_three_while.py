total_rows = int(input("Enter number of rows: "))
total_columns = int(input("Enter number of columns: "))

number = 1
row = 1

while row <= total_rows:

    for column in range(total_columns):
        print(number, end=" ")
        number = number + 1

    print()
    row = row + 1