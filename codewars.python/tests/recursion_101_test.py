import unittest
from unittest import TestCase

from recursion_101 import solve


class Test(TestCase):
    @unittest.skip
    def test_solve1(self):
        self.assertEqual(solve(6, 19), [6, 7])

    @unittest.skip
    def test_solve2(self):
        self.assertEqual(solve(2, 1), [0, 1])

    @unittest.skip
    def test_solve3(self):
        self.assertEqual(solve(22, 5), [0, 1])

    @unittest.skip
    def test_solve4(self):
        self.assertEqual(solve(2, 10), [2, 2])

    @unittest.skip
    def test_solve5(self):
        self.assertEqual(solve(100000000000, 3), [4, 3])


if __name__ == '__main__':
    unittest.main()
