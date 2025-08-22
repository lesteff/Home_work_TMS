def nod(a, b):
    if b == 0:
        return a
    else:
        return nod(b, a % b)

result = nod(12, 18)
print(f"НОД равен {result}")