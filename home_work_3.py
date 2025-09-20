

class Pizza:
    def __init__(self, size):
        self.size = size
        self.cheese = False
        self.pepperoni = False
        self.mushrooms = False
        self.onions = False
        self.bacon = False

    def __str__(self):
        ingredients = []
        if self.cheese:
            ingredients.append("сыр")
        if self.pepperoni:
            ingredients.append("пепперони")
        if self.mushrooms:
            ingredients.append("грибы")
        if self.onions:
            ingredients.append("лук")
        if self.bacon:
            ingredients.append("бекон")

        return f"Пицца {self.size} см с: {', '.join(ingredients)}"


class PizzaBuilder:

    def __init__(self, size):
        self.pizza = Pizza(size)

    def add_cheese(self):
        self.pizza.cheese = True
        return self

    def add_pepperoni(self):
        self.pizza.pepperoni = True
        return self

    def add_mushrooms(self):
        self.pizza.mushrooms = True
        return self

    def add_onions(self):
        self.pizza.onions = True
        return self

    def add_bacon(self):
        self.pizza.bacon = True
        return self

    def build(self):
        return self.pizza

class PizzaDirector:
    def __init__(self, builder):
        self.builder = builder

    def make_pizza(self, ingredients):
        for ingredient in ingredients:
            if ingredient == "cheese":
                self.builder.add_cheese()
            elif ingredient == "pepperoni":
                self.builder.add_pepperoni()
            elif ingredient == "mushrooms":
                self.builder.add_mushrooms()
            elif ingredient == "onions":
                self.builder.add_onions()
            elif ingredient == "bacon":
                self.builder.add_bacon()
        return self.builder.build()


builder1 = PizzaBuilder(27)
director = PizzaDirector(builder1)
pzz1 = director.make_pizza(["cheese", "mushrooms"])
print(f"Готовим {pzz1}")
builder2 = PizzaBuilder(35)
director = PizzaDirector(builder2)
pzz2 = director.make_pizza(["cheese", "pepperoni"])
print(f"Готовим {pzz2}")