
class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def hello():
        print('hello')

    def get_volume(self):
        """
        Volume of a circle is calculated by pi * r^2
        """
        return self.pi * self.radius ** 2


c1 = Circle(5)
c2 = Circle(5)
print(c1.get_volume())
Circle.pi = 4
print(c1.get_volume())
c1.pi = 6
print(c1.get_volume())
print(c2.pi)

