def find_columns_simple(matrix, H):
    with_H = []
    without_H = []
    for j in range(len(matrix[0])):
        if any(matrix[i][j] == H for i in range(len(matrix))):
            with_H.append(j)
        else:
            without_H.append(j)

    return with_H, without_H
matrix = [
    [1, 2, 3, 4],
    [5, 2, 7, 8],
    [9, 10, 3, 12]
]
H = 3
with_H, without_H = find_columns_simple(matrix, H)
print("Исходная матрица:")
for row in matrix:
    print(row)

print(f"\nСтолбцы, содержащие число {H}: {with_H}")
print(f"Столбцы, не содержащие число {H}: {without_H}")