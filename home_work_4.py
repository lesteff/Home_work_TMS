class Sphere:
    def __init__(self, radius=1, x=0, y=0, z=0):
        self.radius = radius
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        pi = 3.14159
        return (4 / 3) * pi * (self.radius ** 3)

    def get_square(self):
        pi = 3.14159
        return 4 * pi * (self.radius ** 2)

    def get_radius(self):
        return self.radius

    def get_center(self):
        return (self.x, self.y, self.z)

    def set_radius(self, radius):
        self.radius = radius

    def set_center(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def is_point_inside(self, x, y, z):
        distance = ((x - self.x) ** 2 +
                    (y - self.y) ** 2 +
                    (z - self.z) ** 2) ** 0.5
        return distance <= self.radius



sphere1 = Sphere()
print("Объем:", sphere1.get_volume())
print("Площадь:", sphere1.get_square())
print("Центр:", sphere1.get_center())

sphere2 = Sphere(2, 1, 2, 3)
print("\nТочка (1,2,3) внутри:", sphere2.is_point_inside(1, 2, 3))
print("Точка (4,5,6) внутри:", sphere2.is_point_inside(4, 5, 6))


sphere2.set_radius(5)
sphere2.set_center(0, 0, 0)
print("\nНовый радиус:", sphere2.get_radius())
print("Новый центр:", sphere2.get_center())