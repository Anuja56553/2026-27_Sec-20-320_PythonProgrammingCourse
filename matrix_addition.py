rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix_a = []
matrix_b = []

print("Enter elements of Matrix A:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix_a.append(row)

print("Enter elements of Matrix B:")
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(int(input()))
    matrix_b.append(row)

result = []

for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix_a[i][j] + matrix_b[i][j])
    result.append(row)

print("Matrix A:", matrix_a)
print("Matrix B:", matrix_b)
print("Sum:", result)