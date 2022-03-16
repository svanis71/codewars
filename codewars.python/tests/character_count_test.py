import unittest
from unittest import TestCase

from character_count import validate_word


class CharacterCountTests(TestCase):
    def testcase_1(self):
        self.assertEqual(validate_word("abcabc"), True)

    def testcase_2(self):
        self.assertEqual(validate_word("Abcabc"), True)

    def testcase_3(self):
        self.assertEqual(validate_word("AbcabcC"), False)

    def testcase_4(self):
        self.assertEqual(validate_word("AbcCBa"), True)

    def testcase_5(self):
        self.assertEqual(validate_word("pippi"), False)

    def testcase_6(self):
        self.assertEqual(validate_word("?!?!?!"), True)

    def testcase_7(self):
        self.assertEqual(validate_word("abc123"), True)

    def testcase_8(self):
        self.assertEqual(validate_word("abcabcd"), False)

    def testcase_9(self):
        self.assertEqual(validate_word("abc!abc!"), True)

    def testcase_10(self):
        self.assertEqual(validate_word("abc:abc"), False)


if __name__ == '__main__':
    unittest.main()
