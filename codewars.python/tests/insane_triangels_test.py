import unittest

'''
https://www.codewars.com/kata/5a331ea7ee1aae8f24000175/train/python
'''
basic_cases = [
    ['B', 'B'],
    ['GB', 'R'],
    ['RRR', 'R'],
    ['RGBG', 'B'],
    ['RBRGBRB', 'G'],
    ['RBRGBRBGGRRRBGBBBGG', 'G']
]


def triangle(row):
    pass


class MyTestCase(unittest.TestCase):
    def _test(self, cases):
        for _in, _out in cases:
            self.assertEqual(triangle(_in), _out)

    def test_something(self):
        self._test(basic_cases)


if __name__ == '__main__':
    unittest.main()
