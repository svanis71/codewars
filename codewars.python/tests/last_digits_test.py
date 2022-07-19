import unittest

from last_digits import solution


class LastDigitsTests(unittest.TestCase):
    def test_1(self):
        # ('Example tests')
        self.assertEqual(solution(1, 1), [1])
        self.assertEqual(solution(123767, 4), [3, 7, 6, 7])
        self.assertEqual(solution(0, 1), [0])
        self.assertEqual(solution(34625647867585, 10), [5, 6, 4, 7, 8, 6, 7, 5, 8, 5])

    def test_2(self):
        # ('d <= 0')
        self.assertEqual(solution(1234, 0), [])
        self.assertEqual(solution(24134, -4), [])

    def test_3(self):
        # ('d > number of digits in n')
        self.assertEqual(solution(1343, 5), [1, 3, 4, 3])


if __name__ == '__main__':
    unittest.main()
