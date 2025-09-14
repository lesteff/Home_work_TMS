class Bus:
    def __init__(self, speed, max_places, max_speed):
        self.speed = speed
        self.max_places = max_places
        self.max_speed = max_speed
        self.passengers = []
        self.free_places = True
        self.place = {}

        for place_number in range(1, max_places + 1):
            self.place[place_number] = None


    def add_pass(self, surname, place_number):
        if place_number not in self.place:
            print("Такого места не существует")

        if self.place[place_number] is not None:
            print("Это место уже занято")
            return False

        self.place[place_number] = surname
        self.passengers.append(surname)
        self._update_free_places()
        print(f"Пасажир {surname} сел на место {place_number}")


    def remove_passenger(self, surname):
        if surname not in self.passengers:
            print(f"{surname} нет в автобусе")
            return False

        for place_number, passenger in self.place.items():
            if passenger == surname:
                self.place[place_number] = None
                break

        self.passengers.remove(surname)
        self._update_free_places()
        print(f"{surname} высажен из автобуса")



    def set_speed(self, new_speed):
        if new_speed > self.max_speed:
            print(f"Скорость не может привышать {self.max_speed} ")
            return False

        self.speed = new_speed
        print(f"Скорость изменилась на {new_speed}")


    def _update_free_places(self):
        self.free_places = len(self.passengers) < self.max_places

    def get_free_places(self):
        free_place = []
        for place_number, passenger in self.place.items():
            if passenger is None:
                free_place.append(place_number)
        return free_place


    def get_busy_places(self):
        busy_place = {}
        for place_number, passenger in self.place.items():
            if passenger is not None:
                busy_place[place_number] = passenger
        return busy_place


    def show_info(self):
        print(f"Текущая скорость {self.speed}")
        print(f"Максимальная скорость {self.max_speed}")
        print(f"Всего мест в автобусе {self.max_places}")
        print(f"Всего пассажиров в автобусе {len(self.passengers)}")
        print(f"Свободных мест в автобусе {self.free_places}")
        print(f"Список пассажиров {self.passengers}")

        for place_number, passenger in self.place.items():
            status = "Свободно" if passenger is None else f"занято : {passenger}"
            print(f"Место {place_number} : {status}")


bus = Bus(speed=40, max_places=10, max_speed=69)
bus.show_info()

bus.add_pass("Максим", 1)
bus.add_pass("Сергей", 7)
bus.add_pass("Полина", 2)

bus.add_pass("Дмитрий", 1)

bus.set_speed(80)

bus.remove_passenger("Максим")

bus.remove_passenger("Ольга")

print("Свободные места : ", bus.get_free_places())
print("Занятные места : ", bus.get_busy_places())


bus.show_info()