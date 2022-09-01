import unittest

from kyu4.rangefinder import rangefinder


class RangeFinderTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rangefinder([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]),
                         '-6,-3-1,3-5,7-11,14,15,17-20')


if __name__ == '__main__':
    unittest.main()
