class Soda:
    def __init__(self, _taste=None):
        self.taste = _taste

    def show_info(self):
        if self.taste is None:
            print("У вас обычная газировка")
        else:
            print(f"У вас газировка с {self.taste} вкусом")


s = Soda()
s.show_info()

