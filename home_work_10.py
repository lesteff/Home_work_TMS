def multiply_columns(matrix, k):

    result = []

    for row in matrix:
        multiplier = row[k]
        new_row = [x * multiplier for x in row]
        result.append(new_row)

    return result

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]


result = multiply_columns(matrix, 1)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nРезультат:")
for row in result:
    print(row)
