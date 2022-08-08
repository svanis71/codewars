from math import dist


# https://www.codewars.com/kata/58e3e62f20617b6d7700120a

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


def triangle_perimeter(t: Triangle) -> float:
    return sum([(dist([t.a.x, t.a.y], [t.b.x, t.b.y])), (dist([t.a.x, t.a.y], [t.c.x, t.c.y])),
                (dist([t.b.x, t.b.y], [t.c.x, t.c.y]))])
