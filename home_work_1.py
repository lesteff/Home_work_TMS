try:
    height = int(input("Введите ваш рост "))
    height = height / 100
    weight = int(input("Введите ваш вес "))
    result = weight / (height * height)
except ValueError:
    print("вы написали не число")
except ZeroDivisionError:
    print("Рост не может быть 0")
except:
    print("Что-то пошло не так... ")
else:
    print("Ваш ИМТ: ", round(result,2))
    if result < 18.5:
        print("Дефицит массы тела")
    elif result < 24.99:
        print("Нормальный вес")
    elif  result < 30:
        print("Предожирение")
    elif result > 30:
        print("Ожирение")
finally:
    print("Расчет вашего ИМТ завершен")
