import unittest

from kyu7.alphabet_war_kyou7 import alphabet_war_kyou7


class AlphabetWarKyou7Tests(unittest.TestCase):
    def test(self):
        self.assertEqual(alphabet_war_kyou7("z"), "Right side wins!")
        self.assertEqual(alphabet_war_kyou7("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war_kyou7("wq"), "Left side wins!")
        self.assertEqual(alphabet_war_kyou7("zzzzs"), "Right side wins!")
        self.assertEqual(alphabet_war_kyou7("wwwwww"), "Left side wins!")
