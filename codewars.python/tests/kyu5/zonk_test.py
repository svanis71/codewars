import unittest

from parameterized import parameterized

from kyu5.zonk import get_score


class ZonkTests(unittest.TestCase):
    @parameterized.expand([(1000, [1, 2, 3, 4, 5, 6], "[1, 2, 3, 4, 5, 6] -> 1000"),
                           (1000, [1, 1, 1], "[1, 1, 1] -> 1000"),
                           (100, [1], "[1] -> 100"),
                           (0, [2], "[2] -> 0"),
                           (0, [3], "[3] -> 0"),
                           (0, [4], "[4] -> 0"),
                           (50, [5], "[5] -> 50"),
                           (0, [6], "[6] -> 0"),
                           (200, [1, 1], "[1, 1] -> 200"),
                           (750, [2, 2, 3, 3, 6, 6], "[2, 2, 3, 3, 6, 6] -> 750"),
                           (0, [3, 2, 6, 4, 4, 6], "[3, 2, 6, 4, 4, 6] -> 0")])
    def test_zonk(self, max_score: int, dice: list[int], descr: str):
        self.assertEqual(max_score, get_score(dice), descr)


if __name__ == '__main__':
    unittest.main()
