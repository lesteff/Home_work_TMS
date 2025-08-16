my_list = [1, 5, 7, 6, 5, 10, 10, 10]
duplicat = []
count = 0

for i in range(len(my_list)):
    num = my_list[i]
    if num in my_list[:i] and num not in duplicat:
        duplicat.append(num)
        count += 1

if duplicat:
    for num in duplicat:
        print(f"Число {num}: встречается {my_list.count(num)} раз(а)")
else:
    print("все числа уникальны")