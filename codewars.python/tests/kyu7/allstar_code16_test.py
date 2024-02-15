import unittest

from parameterized import parameterized

from kyu7.allstar_code16 import no_repeat


class AllStarCodeChallenge16Test(unittest.TestCase):
    @parameterized.expand([("aabbccdde", "e"),
                           ("wxyz", "w"),
                           ("testing", "e"),
                           ("codewars", "c"),
                           ("Testing", "T")
                           ])
    def test_something(self, s: str, expected_first_no_repeating_char: str):
        self.assertEqual(no_repeat(s), expected_first_no_repeating_char)


if __name__ == '__main__':
    unittest.main()
