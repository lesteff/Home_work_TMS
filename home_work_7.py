n = int(input("Введите сколько стоит телефон: "))
k = int(input("Сколько маша будет откладывать?: "))
count_money = 0
count = 0

while count_money != n:
    count += 1
    if count % 7 != 0:
        count_money += k
    else:
        count - k

print(f"Маша накопит на телефон за {count} дней")

