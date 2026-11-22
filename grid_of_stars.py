grid_size = int(input("Enter grid size: "))

for row in range(grid_size):
    for column in range(grid_size):
        print("*", end=" ")
    print()