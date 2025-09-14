class BeeElephant:

    def __init__(self, bee, elephant):
        self.bee = bee
        self.elephant = elephant

    def fly(self):
        if self.bee > self.elephant:
            return True
        else:
            return False

    def trumpet(self):
        if self.elephant > self.bee:
            print("tu-tu-doo-doo")
        else:
            print("wzzzz")



    def eat(self, meal, value):
        if  value < 0 :
            raise ValueError("Не может быть больше 100 и меньше 0")
        if value > 100:
            raise ValueError("Не может быть больше 100 и меньше 0")
        if meal == 'nectar':
            self.elephant -= value
            self.bee += value
            print(f'Новое значение Elephant =  {self.elephant} уменьшилось на {value}')
            print(f'Новое значение Bee =  {self.bee} увеличилось на {value}')
        elif meal == 'grass':
            self.elephant += value
            self.bee -= value
            print(f'Новое значение Elephant =  {self.elephant} увеличилось на {value}')
            print(f'Новое значение Bee =  {self.bee} уменьшилось на {value}')


b = BeeElephant(20, 15)
print(b.fly())
b.trumpet()
b.eat('nectar', 88)
b.eat('grass', 20)
