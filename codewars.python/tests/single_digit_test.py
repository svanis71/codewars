import unittest

from single_digit import single_digit


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(single_digit(5665), 5)

    def test_2(self):
        self.assertEqual(single_digit(123456789), 1)


if __name__ == '__main__':
    unittest.main()
