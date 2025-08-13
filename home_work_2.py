import math
i = float(input("Введите годовую процентную ставку:")) / 100
s = float(input("Введите сумму займа:"))
n = int(input("Кол-во месяцев, на которые взят кредит:"))

p = i / 12

m = (s * p * math.pow(1 + p, n)) / (math.pow(1 + p, n) - 1)
all_pay = m * n
overpayment = all_pay - s
print("Ежемесячная выплата по кредиту :", m)
print("Пользователь заплатит всего банку: ", all_pay)
print("Переплата по кредиту составила: ",overpayment)