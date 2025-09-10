class Math:
    def __init__(self):
        pass


    def addition(self, x, y):
        result = x + y
        print(result)
    def subtraction(self, x, y):
        result = x - y
        print(result)
    def multiplication(self, x, y):
        result = x * y
        print(result)
    def division(self, x, y):
        if y != 0:
            result = x / y
            print(int(result))
        else:
            print("Деление на ноль")


m = Math()

m.addition(5, 6)
m.subtraction(10, 20)
m.multiplication(10, 5)
m.division(10 , 0)