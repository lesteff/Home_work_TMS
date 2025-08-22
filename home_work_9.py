def matrix_analysis(matrix):

    total = sum(sum(row) for row in matrix)
    cols = len(matrix[0])

    # Суммы по столбцам
    col_sums = [sum(matrix[i][j] for i in range(len(matrix))) for j in range(cols)]

    # Проценты
    col_percents = [(s / total) * 100 for s in col_sums]

    return total, col_percents


# Использование
matrix = [
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
]

total, percents = matrix_analysis(matrix)

print(f"сумма элементов матрицы: {total}")
for j, p in enumerate(percents):
    print(f"Столбец {j}: {p:.1f}% ({p:.2f}%)")