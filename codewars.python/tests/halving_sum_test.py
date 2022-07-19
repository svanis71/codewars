import unittest

from halving_sum import halving_sum


class HavingSumTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(halving_sum(25), 47)
        self.assertEqual(halving_sum(127), 247)


if __name__ == '__main__':
    unittest.main()
