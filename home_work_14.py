def add_even_ones_column(matrix):
    result = []
    for row in matrix:
        count_ones = sum(row)
        new_element = 0 if count_ones % 2 == 0 else 1
        result.append(row + [new_element])

    return result


matrix = [
    [1, 0, 1, 0],
    [1, 1, 1, 0],
    [0, 0, 0, 1]
]

new_matrix = add_even_ones_column(matrix)

print("Исходная матрица:")
for row in matrix:
    print(row)

print("\nМатрица с новым столбцом:")
for row in new_matrix:
    print(row)