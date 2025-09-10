class Car:
    def __init__(self, typer, color, year):
        self.typer = typer
        self.color = color
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def change_color(self,new_color):
        self.color = new_color
        print(self.color)
    def change_typer(self, new_typer):
        self.typer = new_typer
        print(self.typer)
    def change_year(self, new_year):
        self.year = new_year
        print(self.year)

my_car = Car("дизель","синий",2000)

my_car.start()
my_car.stop()
my_car.change_color("красный")
my_car.change_typer("бензин")
my_car.change_year(2015)
