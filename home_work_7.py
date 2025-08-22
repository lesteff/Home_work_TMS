import random
def create_matrix(m, n, min_val=0, max_val=100):

    matrix = []
    for i in range(m):
        row = []
        for j in range(n):
            row.append(random.randint(min_val, max_val))
        matrix.append(row)
    return matrix

rows = 3
cols = 4
matrix = create_matrix(rows, cols)

print(f"Матрица {rows}x{cols}:")
for row in matrix:
    print(row)