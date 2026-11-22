total_rows = int(input("Enter number of rows: "))
total_columns = int(input("Enter number of columns: "))

number = 1

for row in range(total_rows):
    for column in range(total_columns):
        print(number, end=" ")
        number = number + 1
    print()