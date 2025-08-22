def calculator(value_calc):
    if value_calc == 0:
        return [0]

    my_list = []
    while value_calc > 0:
        my_list.append(value_calc % 2)
        value_calc = value_calc // 2

    my_list.reverse()
    return my_list


binary_number = calculator(100)
print(binary_number)



