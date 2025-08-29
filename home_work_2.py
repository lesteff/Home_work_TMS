try:
    my_list = [
        '+',
        '-',
        '*',
        '/']
    first_value = int(input("Введите первое число: "))
    second_value = int(input("Введите второе число: "))
    operation_value = input("Введите знак: ")
except ValueError:
    print('Вы передали не число!')
else:
    if operation_value == '/':
        if second_value == 0:
            print("Деление на ноль запрещено!")
        else:
            result = first_value / second_value
            print(f"Результат {result}")
    elif operation_value == '*':
        result = first_value * second_value
        print(f"Результат {result}")
    elif operation_value == '+':
        result = first_value + second_value
        print(f"Результат {result}")
    elif operation_value == '-':
        result = first_value - second_value
        print(f"Результат {result}")
    elif operation_value not in my_list:
        print("Не верный знак")
finally:
    print("Расчет завершен!")

