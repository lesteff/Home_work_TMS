def find_diagonals_sum(matrix):
    main_diag_sum = 0
    anti_diag_sum = 0
    n = len(matrix)
    for i in range(n):
        main_diag_sum += matrix[i][i]
        anti_diag_sum += matrix[i][n - 1 - i]

    return main_diag_sum, anti_diag_sum


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

main_sum, anti_sum = find_diagonals_sum(matrix)

print("Матрица:")
for row in matrix:
    print(row)

print(f"\nГлавная диагональ (1,5,9): {main_sum}")
print(f"Побочная диагональ (3,5,7): {anti_sum}")