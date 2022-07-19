import unittest

from alphabet_war import alphabet_war_letters_massacre


class AlphabetWarLettersTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(alphabet_war_letters_massacre("z"), "Right side wins!")
        self.assertEqual(alphabet_war_letters_massacre("****"), "Let's fight again!")
        self.assertEqual(alphabet_war_letters_massacre("z*dq*mw*pb*s"), "Let's fight again!")
        self.assertEqual(alphabet_war_letters_massacre("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war_letters_massacre("zz*zzs"), "Right side wins!")
        self.assertEqual(alphabet_war_letters_massacre("sz**z**zs"), "Left side wins!")
        self.assertEqual(alphabet_war_letters_massacre("z*z*z*zs"), "Left side wins!")
        self.assertEqual(alphabet_war_letters_massacre("*wwwwww*z*"), "Left side wins!")
        self.assertEqual(alphabet_war_letters_massacre("w****z"), "Let's fight again!")
        self.assertEqual(alphabet_war_letters_massacre("mb**qwwp**dm"), "Let's fight again!")


if __name__ == '__main__':
    unittest.main()
