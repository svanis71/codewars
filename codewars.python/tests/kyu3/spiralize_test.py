import unittest

from kyu3.spiralize import spiralize


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual([[1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 1],
                          [1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1]], spiralize(5))

    def test_size_10(self):
        self.assertEqual([[1, 1, 1, 1, 1, 1, 1, 1],
                          [0, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 1, 0, 1],
                          [1, 0, 1, 0, 0, 1, 0, 1],
                          [1, 0, 1, 1, 1, 1, 0, 1],
                          [1, 0, 0, 0, 0, 0, 0, 1],
                          [1, 1, 1, 1, 1, 1, 1, 1]], spiralize(8))


if __name__ == '__main__':
    unittest.main()
