import unittest

from kyu5.largest_sum import largest_sum


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(largest_sum([-1, -2, -3]), 0)

    def test_2(self):
        self.assertEqual(largest_sum([]), 0)

    def test_3(self):
        self.assertEqual(largest_sum([1, 2, 3, 4]), 10)

    def test_4(self):
        self.assertEqual(largest_sum([31, -41, 59, 26, -53, 58, 97, -93, -23, 84]), 187)


if __name__ == '__main__':
    unittest.main()
