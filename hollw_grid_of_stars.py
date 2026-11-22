grid_size = int(input("Enter grid size: "))

for row in range(grid_size):
    for column in range(grid_size):

        if row == 0 or row == grid_size - 1 or column == 0 or column == grid_size - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()