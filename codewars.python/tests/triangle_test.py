import unittest

from triangle import triangle

basic_cases = [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G']
]


class TriangleTest(unittest.TestCase):
    def _test(self, cases):
        for _in, _out in cases:
            self.assertEqual(triangle(_in), _out)

    def test_something(self):
        self._test(basic_cases)


if __name__ == '__main__':
    unittest.main()
