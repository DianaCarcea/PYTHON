import math


class Shape:
    def perimeter(self):
        pass

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, rad):
        if rad <= 0:
            raise ValueError("Raza trebuie sa fie un numar pozitiv!")
        self._radius = rad

    def perimeter(self):
        f_perimeter = 2 * math.pi * self._radius  # P=2*pi*r
        return round(f_perimeter, 2)

    def area(self):
        f_area = math.pi * (self._radius * self._radius)  # A=pi*r^2
        return round(f_area, 2)

    def get_radius(self):
        return self._radius


class Rectangle(Shape):
    def __init__(self, length, width):
        if length <= 0 or width <= 0:
            raise ValueError("Lugimea si latimea trebuie sa fie pozitive!")
        self._length = length
        self._width = width

    def perimeter(self):
        f_perimeter = 2 * (self._length + self._width)  # P=2*L*l
        return round(f_perimeter, 2)

    def area(self):
        f_area = self._length * self._width  # A=L*l
        return round(f_area, 2)

    def get_dimensions(self):
        return self._length, self._width


class Triangle(Shape):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Laturile trebuie sa fie pozitive.")
        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Nu se poate forma un triunghi cu aceste lungimi de laturi.")
        self.a = a
        self.b = b
        self.c = c

    def perimeter(self):
        f_perimeter = self.a+self.b+self.c  # P=a+b+c
        return round(f_perimeter, 2)

    def area(self):
        p = self.perimeter()/2  # Semi-perimeter
        f_area = math.sqrt(p*(p-self.a)*(p-self.b)*(p-self.c))  # Heron: A=rad( p⋅(p−a)⋅(p−b)⋅(p−c) )
        return round(f_area, 2)

    def get_sides(self):
        return self.a, self.b, self.c


if __name__ == '__main__':
    print("---------------------------------")
    circle = Circle(5)
    print("Cerc cu raza:", circle.get_radius())
    print("Arie cerc:", circle.area())
    print("Perimetru cerc:", circle.perimeter())

    print("---------------------------------")
    rectangle = Rectangle(2, 5)
    print(f"Dreptunghi cu lugime={rectangle.get_dimensions()[0]} latime={rectangle.get_dimensions()[1]}")
    print("Arie dreptunghi:", rectangle.area())
    print("Perimetru dreptunghi:", rectangle.perimeter())

    print("---------------------------------")
    triangle = Triangle(4, 7, 10)
    print(f"Triunghi cu laturile: a={triangle.get_sides()[0]} b={triangle.get_sides()[1]} c={triangle.get_sides()[2]}")
    print("Arie triunghi:", triangle.area())
    print("Perimetru triunghi:", triangle.perimeter())
