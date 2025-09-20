from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        print("гаф гаф")

class Cat(Animal):
    def speak(self):
        print("Мяу Мяу")


class AnimalFactory:
    def create_animal(self, value):
        if value == 'dog':
            return Dog()
        elif value == 'cat':
            return Cat()


pets = AnimalFactory()

dog = pets.create_animal('dog')
cat = pets.create_animal('cat')

dog.speak()
cat.speak()

