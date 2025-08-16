my_list = [5, 6, 7, 1, 2, 3, 4]

low = 0
high = len(my_list) - 1
position = -1
value_search = int(input("Введите число которое хотите найти: "))

while low <= high:
    mid = (low + high) // 2
    guess = my_list[mid]

    if guess == value_search:
        position = mid
        break

    # Левая часть отсортирована
    if my_list[low] <= guess:
        if my_list[low] <= value_search < guess:
            high = mid - 1
        else:
            low = mid + 1
    # Правая часть отсортирована
    else:
        if guess < value_search <= my_list[high]:
            low = mid + 1
        else:
            high = mid - 1

if position != -1:
    print(f"Элемент {value_search} найден на позиции {position}")
else:
    print(f"{value_search} нет в данном списке")
