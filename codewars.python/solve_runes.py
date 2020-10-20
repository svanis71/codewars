import unittest
import re

OP = {
    '*': lambda a, b: a * b,
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
}


def solve_runes(s):
    for i in '0123456789':
        if i not in s:
            t = s.replace('?', i)
            n1, op, n2, eq = re.findall(r'(-?[\d]+)([*+-])(-?[\d]+)[=](-?[\d]+)', t)[0]
            if not re.search(r'^-?0\d+', n1) and not re.search(r'^-?0\d+', n2) and not re.search(r'^-?0\d+', eq):
                if OP[op](int(n1), int(n2)) == int(eq):
                    return int(i)
    return -1


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
