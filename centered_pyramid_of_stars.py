total_rows = int(input("Enter number of rows: "))

for row in range(1, total_rows + 1):

    for space in range(total_rows - row):
        print(" ", end=" ")

    for star in range(2 * row - 1):
        print("*", end=" ")

    print()