import unittest

from solve_runes import solve_runes, OP


class MyTestCase(unittest.TestCase):
    def test_plus(self):
        self.assertEqual(2, OP['+'](1, 1))

    def test_minus(self):
        self.assertEqual(2, OP['-'](3, 1))

    def test_multiply(self):
        self.assertEqual(4, OP['*'](2, 2))

    def test1(self):
        self.assertEqual(2, solve_runes("1+1=?"), "Answer for expression '1+1=?' ")

    def test2(self):
        self.assertEqual(6, solve_runes("123*45?=5?088"), "Answer for expression '123*45?=5?088' ")

    def test3(self):
        self.assertEqual(0, solve_runes("-5?*-1=5?"), "Answer for expression '-5?*-1=5?' ")

    def test4(self):
        self.assertEqual(-1, solve_runes("19--45=5?"), "Answer for expression '19--45=5?' ")

    def test5(self):
        self.assertEqual(5, solve_runes("??*??=302?"), "Answer for expression '??*??=302?' ")

    def test6(self):
        self.assertEqual(2, solve_runes("?*11=??"), "Answer for expression '?*11=??' ")

    def test7(self):
        self.assertEqual(2, solve_runes("??*1=??"), "Answer for expression '??*11=??' ")

    def test8(self):
        self.assertEqual(8, solve_runes("-?56373--9216=-?47157"), "Answer for expression '??*11=??' ")


if __name__ == '__main__':
    unittest.main()
