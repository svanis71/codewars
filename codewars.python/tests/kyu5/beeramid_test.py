import unittest

from parameterized import parameterized

from kyu5.beeramid import beeramid


class BeeramidTests(unittest.TestCase):
    @parameterized.expand([(9, 2, 1), (21, 1.5, 3), (-1, 4, 0), (1500, 2, 12), (5000, 3, 16)])
    def test_beeramid(self, bonus: int, beer_price: float, expected_result: int):
        self.assertEqual(beeramid(bonus, beer_price), expected_result)


if __name__ == '__main__':
    unittest.main()
