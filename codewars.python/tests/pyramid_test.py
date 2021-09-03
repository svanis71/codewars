import unittest

from pyramid_kata import pyramid


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(pyramid(0), [])
        self.assertEqual(pyramid(1), [[1]])
        self.assertEqual(pyramid(2), [[1], [1, 1]])
        self.assertEqual(pyramid(3), [[1], [1, 1], [1, 1, 1]])


if __name__ == '__main__':
    unittest.main()
