from unittest import TestCase

from parameterized import parameterized

from kyu8.allstarcode18 import str_count


class AllstarCodeChallenge18_Tests(TestCase):
    @parameterized.expand([('hello', 'l', 2),
                           ('hello', 'e', 1),
                           ('codewars', 'c', 1),
                           ('ggggg', 'g', 5),
                           ('hello world', 'o', 2),
                           ('', 'z', 0)])
    def tests(self, word: str, letter: str, expected_cnt: int):
        self.assertEqual(expected_cnt, str_count(word, letter))
