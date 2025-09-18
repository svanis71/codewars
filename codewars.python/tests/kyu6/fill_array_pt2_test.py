import unittest

from kyu6.fill_array_pt2 import squares, num_range, rand_range, primes


class MyTestCase(unittest.TestCase):
    def test_squares(self):
        self.assertEqual(squares(5), [1, 4, 9, 16, 25])

    def test_primes(self):
        self.assertEqual(primes(6), [2, 3, 5, 7, 11, 13])

    def test_num_range(self):
        self.assertEqual(num_range(6, 3, 2), [3, 5, 7, 9, 11, 13])

    def test_rand_range(self):
        rands = rand_range(4, 5, 10)
        self.assertEqual(len(rands), 4)
        self.assertTrue(min(rands) >= 5)
        self.assertTrue(max(rands) < 10)

    def test_empty_list(self):
        self.assertEqual(squares(0), [])
        self.assertEqual(num_range(0, 3, 2), [])
        self.assertEqual(rand_range(0, 5, 10), [])
        self.assertEqual(primes(0), [])


if __name__ == '__main__':
    unittest.main()
