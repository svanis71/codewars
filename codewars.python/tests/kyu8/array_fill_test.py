import unittest

from kyu8.array_fill import array_fill


class ArrayFillTests(unittest.TestCase):
    def test_0(self):
        self.assertEqual(array_fill(1), [0])

    def test_1(self):
        self.assertEqual(array_fill(4), [0, 1, 2, 3])

    def test_2(self):
        self.assertEqual(array_fill(0), [])

    def test_3(self):
        self.assertEqual(array_fill(), [])


if __name__ == '__main__':
    unittest.main()
