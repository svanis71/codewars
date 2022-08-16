import unittest

from woodcut import wood_cut


class WoodCutTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(114, wood_cut([232, 124, 456], 7))

    def test_2(self):
        self.assertEqual(38, wood_cut([232, 124, 456], 20))

    def test_3(self):
        self.assertEqual(456, wood_cut([232, 124, 456], 1))

    def test_4(self):
        self.assertEqual(232, wood_cut([232, 124, 456], 2))

    def test_5(self):
        self.assertEqual(228, wood_cut([232, 124, 456], 3))

    def test_6(self):
        self.assertEqual(0, wood_cut([1, 1, 1], 4))

    def test_7(self):
        self.assertEqual(1, wood_cut([1, 1, 1], 3))

    def test_8(self):
        self.assertEqual(1073741823, wood_cut([200000000, 2147483645, 2147483646, 2147483647], 4))


if __name__ == '__main__':
    unittest.main()
