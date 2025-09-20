from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def execute(self, a, b):
        pass

class Addition(Strategy):
    def execute(self, a, b):
        return a + b

class Subtraction(Strategy):
    def execute(self, a, b):
        return a - b


class Multiplication(Strategy):
    def execute(self, a, b):
        return a * b


class Division(Strategy):
    def execute(self, a, b):
        if b == 0:
            raise ValueError("Делить на ноль нельзя!")
        return a / b


class Calculator:
    def __init__(self):
        self.strategy = None

    def set_strategy(self, strategy):
        if not isinstance(strategy, Strategy):
            raise TypeError("Стратегия должна наследоваться от Strategy")
        self._strategy = strategy

    def calculate(self, a, b):
        if self._strategy is None:
            raise ValueError("Стратегия не установлена")
        return self._strategy.execute(a, b)

calculator = Calculator()


calculator.set_strategy(Addition())
result = calculator.calculate(20, 25)
print(f"20 + 25 = {result}")


calculator.set_strategy(Subtraction())
result = calculator.calculate(20, 25)
print(f"20 - 25 = {result}")


calculator.set_strategy(Multiplication())
result = calculator.calculate(20, 25)
print(f"20 * 25 = {result}")

calculator.set_strategy(Division())
result = calculator.calculate(10, 5)
print(f"10 / 5 = {int(result)}")

try:
    result = calculator.calculate(10, 0)
except ValueError as e:
    print(f"Ошибка: {e}")


