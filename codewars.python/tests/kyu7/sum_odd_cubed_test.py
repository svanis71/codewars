import unittest

from kyu7.sum_odd_cubed import cube_odd


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(cube_odd([1, 2, 3, 4]), 28)
        self.assertEqual(cube_odd([-3, -2, 2, 3]), 0)
        self.assertEqual(cube_odd(["a", 12, 9, "z", 42]), None)

    def test_boolean(self):
        self.assertEqual(cube_odd([True, False, 2, 4, 1]), None)


if __name__ == '__main__':
    unittest.main()
