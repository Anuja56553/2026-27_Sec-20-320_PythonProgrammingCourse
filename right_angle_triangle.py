total_rows = int(input("Enter number of rows: "))
symbol = input("Enter a symbol: ")

for row in range(1, total_rows + 1):
    for column in range(row):
        print(symbol, end=" ")
    print()