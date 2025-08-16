my_list = [1, 67, 24, 43, 89, 27, 55]
my_list = sorted(my_list)
low = 0
hight = len(my_list)
position = -1
value_search = int(input("Введите число которое хотите найти: "))

while low <= hight:
    mid = (low + hight)//2
    guess = my_list[mid]
    if guess == value_search:
        position = mid
        break
    elif guess > value_search:
        hight = mid - 1
    else:
        low = mid + 1

if position != -1:
    print(f"Элемент {value_search} найден на позиции {position}")
else:
    print(f"{value_search} нет в данном списке")


