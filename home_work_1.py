def binary_search(value_a):
    my_list = [15, 25, 34, 8, 9, 20]
    my_list = sorted(my_list)
    low = 0
    hight = len(my_list)
    position = -1

    while low <= hight:
        mid = (low + hight) // 2
        guess = my_list[mid]
        if guess == value_a:
            position = mid
            break
        elif guess > value_a:
            hight = mid - 1
        else:
            low = mid + 1

    if position != -1:
        print(f"Элемент {value_a} найден на позиции {position}")
    else:
        print(f"{value_a} нет в данном списке")


binary_search(9)