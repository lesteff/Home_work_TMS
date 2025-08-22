def find_min_max(matrix):

    min_val = min(min(row) for row in matrix)
    max_val = max(max(row) for row in matrix)

    for i, row in enumerate(matrix):
        if min_val in row:
            min_i, min_j = i, row.index(min_val)
        if max_val in row:
            max_i, max_j = i, row.index(max_val)

    return (min_val, min_i, min_j), (max_val, max_i, max_j)


# Использование
matrix = [
    [45, 12, 87, 23],
    [91, 34, 56, 78],
    [5, 67, 89, 10]
]

(min_val, min_i, min_j), (max_val, max_i, max_j) = find_min_max(matrix)

print(f"Минимум: {min_val} [строка {min_i}, столбец {min_j}]")
print(f"Максимум: {max_val} [строка {max_i}, столбец {max_j}]")