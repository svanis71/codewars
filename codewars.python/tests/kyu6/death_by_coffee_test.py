import unittest

from parameterized import parameterized

from kyu6.death_by_coffee import coffee_limits


class MyTestCase(unittest.TestCase):
    @parameterized.expand(
        [(1950, 1, 19, [2645, 1162]),
         (1964, 11, 28, [0, 11]),
         (1965, 9, 4, [0, 0]),
         (1965, 12, 11, [111, 0]),
         (1880, 3, 1, [0, 3909])])
    def test_death_by_coffe_limits(self, y: int, m: int, d: int, expected: list[int]):
        self.assertEqual(expected, coffee_limits(y, m, d))


if __name__ == '__main__':
    unittest.main()
