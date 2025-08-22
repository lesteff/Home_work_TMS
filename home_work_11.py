def sum_rows(matrix, L):
    result = []
    L_row = matrix[L]
    for row in matrix:
        new_row = [row[i] + L_row[i] for i in range(len(row))]
        result.append(new_row)
    return result


matrix = [
    [1, 2],
    [3, 4],
    [5, 6]
]

result = sum_rows(matrix, 1)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультат (каждая строка + строка 1):")
for row in result:
    print(row)