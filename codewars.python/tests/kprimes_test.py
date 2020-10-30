import unittest

from kprimes import kprimes, puzzle


class MyTestCase(unittest.TestCase):
    def test_kprimes(self):
        tests = [
            ([4, 6, 9, 10, 14, 15, 21, 22, 25, 26, 33, 34, 35, 38, 39, 46, 49, 51, 55, 57, 58, 62, 65, 69, 74, 77, 82,
              85, 86, 87, 91, 93, 94, 95], (2, 0, 100)),
            ([8, 12, 18, 20, 27, 28, 30, 42, 44, 45, 50, 52, 63, 66, 68, 70, 75, 76, 78, 92, 98, 99], (3, 0, 100)),
            ([500, 520, 552, 567, 588, 592, 594], (5, 500, 600)),
            ([1020, 1026, 1032, 1044, 1050, 1053, 1064, 1072, 1092, 1100], (5, 1000, 1100))
        ]
        for expected, test_val in tests:
            k, start, end = test_val
            self.assertEqual(expected, kprimes(k, start, end), f'Test kprimes({k}, {start}, {end})')

    def test_puzzle(self):
        self.assertEqual(1, puzzle(138), "Test for puzzle(138)")
        self.assertEqual(2, puzzle(143), "Test for puzzle(143)")

if __name__ == '__main__':
    unittest.main()
