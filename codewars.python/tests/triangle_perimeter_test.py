import unittest
from math import sqrt


class Point:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @x.setter
    def x(self, value):
        self._x = value

    @y.setter
    def y(self, value):
        self._y = value


class Triangle:
    def __init__(self, p1: Point, p2: Point, p3: Point):
        self._a = p1
        self._b = p2
        self._c = p3

    @property
    def a(self) -> Point:
        return self._a

    @property
    def b(self) -> Point:
        return self._b

    @property
    def c(self) -> Point:
        return self._c

    @a.setter
    def a(self, value):
        self._a = value

    @b.setter
    def b(self, value):
        self._b = value

    @c.setter
    def c(self, value):
        self._c = value


def triangle_perimeter(triangle: Triangle) -> float:
    a, b, c = triangle.a, triangle.b, triangle.c
    d_ab = sqrt((b.x - a.x) ** 2 + (b.y - a.y) ** 2)
    d_ac = sqrt((c.x - a.x) ** 2 + (c.y - a.y) ** 2)
    d_bc = sqrt((c.x - b.x) ** 2 + (c.y - b.y) ** 2)
    return d_ab + d_ac + d_bc


class TrianglePerimeterTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(120, round(triangle_perimeter(
            Triangle(Point(10, 10), Point(40, 10), Point(10, 50))
        ), 6))

    def test_2(self):
        self.assertEqual(135.314734, round(triangle_perimeter(
            Triangle(Point(15, -10), Point(40, 20), Point(20, 50))
        ), 6))


if __name__ == '__main__':
    unittest.main()
