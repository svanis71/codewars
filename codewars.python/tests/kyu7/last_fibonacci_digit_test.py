import unittest

from kyu7.last_fibonacci_digit import get_last_digit


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, get_last_digit(1))

    def test_21(self):
        self.assertEqual(6, get_last_digit(21))

    def test_302(self):
        self.assertEqual(1, get_last_digit(302))

    def test_4003(self):
        self.assertEqual(7, get_last_digit(4003))

    def test_50004(self):
        self.assertEqual(8, get_last_digit(50004))


if __name__ == '__main__':
    unittest.main()
