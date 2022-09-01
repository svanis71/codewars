import unittest

from kyu4.palindrome_oneline import palindrome


class MyTestCase(unittest.TestCase):
    def test_2(self):
        length, strng = 3, "ab"
        self.assertEqual("aba", palindrome(length, strng))

    def test_3(self):
        length, strng = 10, "ab"
        self.assertEqual("ababaababa", palindrome(length, strng))

    def test_4(self):
        length, strng = 20, "abcd"
        self.assertEqual("abcdabcdabbadcbadcba", palindrome(length, strng))

    def test_5(self):
        length, strng = 1, "a"
        self.assertEqual("a", palindrome(length, strng))

    def test_6(self):
        length, strng = 51, "abcdefghijklmnopqrstuvwxyz"
        self.assertEqual("abcdefghijklmnopqrstuvwxyzyxwvutsrqponmlkjihgfedcba", palindrome(length, strng))


if __name__ == '__main__':
    unittest.main()
