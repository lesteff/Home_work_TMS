class Product:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    def get_name(self):
        return self.__name

    def get_store(self):
        return self.__store

    def get_price(self):
        return self.__price


    def display(self):
        print(f"Товар: {self.__name}, Магазин: {self.__store}, Цена: {self.__price} руб.")


    def __add__(self, other):
        return self.__price + other.__price


    def __str__(self):
        return f"Товар: {self.__name}, Магазин: {self.__store}, Цена: {self.__price} руб."


class Warehouse:
    def __init__(self):
        self.__products = []  # массив товаров


    def add_product(self, product):
        self.__products.append(product)


    def display_by_index(self, index):
        if 0 <= index < len(self.__products):
            self.__products[index].display()
        else:
            print("Ошибка: неверный индекс!")

    # Вывод информации по имени товара
    def display_by_name(self, name):
        found = False
        for product in self.__products:
            if product.get_name().lower() == name.lower():
                product.display()
                found = True
        if not found:
            print(f"Товар '{name}' не найден!")


    def sort_by_name(self):
        self.__products.sort(key=lambda x: x.get_name())


    def sort_by_store(self):
        self.__products.sort(key=lambda x: x.get_store())


    def sort_by_price(self):
        self.__products.sort(key=lambda x: x.get_price())


    def display_all(self):
        print("\nВсе товары на складе:")
        for i, product in enumerate(self.__products):
            print(f"{i}: {product}")


    def get_product(self, index):
        if 0 <= index < len(self.__products):
            return self.__products[index]
        return None



warehouse = Warehouse()


warehouse.add_product(Product("Телевизор", "5 элемент", 4000))
warehouse.add_product(Product("Компьютер", "Электросила", 5000))
warehouse.add_product(Product("Смартфон", "МТС", 2000))
warehouse.add_product(Product("Ноутбук", "На связи", 3500))


warehouse.display_all()


warehouse.display_by_index(2)


warehouse.display_by_name("Телевизор")


warehouse.sort_by_name()
warehouse.display_all()

warehouse.sort_by_price()
warehouse.display_all()

product1 = warehouse.get_product(0)
product2 = warehouse.get_product(1)
if product1 and product2:
    total = product1 + product2  # Используем перегруженное сложение
    print(f"Сумма цен: {total} руб.")


