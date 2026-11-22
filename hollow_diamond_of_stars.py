total_rows = int(input("Enter number of rows: "))

for row in range(1, total_rows + 1):

    for space in range(total_rows - row):
        print(" ", end=" ")

    for column in range(1, 2 * row):

        if column == 1 or column == 2 * row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

for row in range(total_rows - 1, 0, -1):

    for space in range(total_rows - row):
        print(" ", end=" ")

    for column in range(1, 2 * row):

        if column == 1 or column == 2 * row - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()