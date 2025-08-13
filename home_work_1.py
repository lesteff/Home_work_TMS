import math
#Задание первое

#A
a = int(input("Введите число a:"))
b = int(input("Введите число b:"))
x = int(input("Введите число x:"))

expression_1 = a**2/3
expression_2 = a**2 + 4/ b
expression_3 = math.sqrt(a**2 + 4)
expression_4 = math.sqrt((a**2 + 4)**3)
y_a = expression_1 + expression_2 + expression_3 / 4 + expression_4 / 4
print("Y = ",y_a)

#B

y_b = math.cos(x) + math.sin(x)

print("Y:", y_b)

#C

y_c = (math.cos(x ** 2) ** 2) ** (1/3) + (math.sin(2 * x - 1)) ** 2

print("Y: ", y_c)

#D

y_d = 5 * x + 3 * (x ** 2) * math.sqrt(1 + (math.sin(x)) ** 2)

print("Y:",y_d)




