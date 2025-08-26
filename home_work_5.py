from functools import reduce

rooms = [
    {"name": "Kitchen", "length": 6, "width": 4},
    {"name": "Room 1", "length": 5.5, "width": 4.5},
    {"name": "Room 2", "length": 5, "width": 4},
    {"name": "Room 3", "length": 7, "width" : 6.3}
]


squares = list(map(lambda room: room['length'] * room['width'], rooms))
print(f"Площадь отдельных комнат {squares}")

all_squares = reduce(lambda x, y: x + y, squares)
print(f"общая площадь квартиры : {all_squares}")