def generator(seq):
    i = 0
    while True:
        yield seq[i]
        i = (i + 1) % len(seq)

try:
    n = int(input("Количество чисел: "))
    gen = generator([1, 2, 3])
    print("-".join(str(next(gen)) for _ in range(n)))
except ValueError:
    print("Ошибка ввода!")