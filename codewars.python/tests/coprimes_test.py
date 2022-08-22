import unittest

from coprimes import coprimes


class CoprimesTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual([1], coprimes(2))
        self.assertEqual([1, 2], coprimes(3))
        self.assertEqual([1, 5], coprimes(6))
        self.assertEqual([1, 3, 7, 9], coprimes(10))
        self.assertEqual([1, 3, 7, 9, 11, 13, 17, 19], coprimes(20))
        self.assertEqual([1, 2, 3, 4, 6, 7, 8, 9, 11, 12, 13, 14, 16, 17, 18, 19, 21, 22, 23, 24], coprimes(25))
        self.assertEqual([1, 7, 11, 13, 17, 19, 23, 29], coprimes(30))


if __name__ == '__main__':
    unittest.main()
