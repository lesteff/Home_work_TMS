def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

try:
    n = int(input("Введите количество чисел Фибоначчи: "))

    if n <= 0:
        print("Число должно быть положительным.")
    else:
        print("Последовательность Фибоначчи:")
        print(", ".join(str(num) for num in fibonacci_generator(n)))

except ValueError:
    print("Ошибка: введите целое число.")