total_rows = int(input("Enter number of rows: "))

for row in range(total_rows, 0, -1):
    for column in range(row):
        print("*", end=" ")
    print()