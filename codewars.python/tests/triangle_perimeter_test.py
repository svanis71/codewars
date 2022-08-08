import unittest

from triangle_perimeter import Point, Triangle, triangle_perimeter


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
