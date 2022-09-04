import unittest

from kyu6.string_tops import tops


class StringTopsTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual("", tops(""))

    def test_2(self):
        self.assertEqual("2", tops("12"))

    def test_3(self):
        self.assertEqual("3pgb", tops("abcdefghijklmnopqrstuvwxyz12345"))

    def test_4(self):
        self.assertEqual("M3pgb", tops("abcdefghijklmnopqrstuvwxyz1236789ABCDEFGHIJKLMN"))


if __name__ == '__main__':
    unittest.main()
