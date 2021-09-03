import unittest

from alphabet_war import alphabet_war_reinforces


class AlphabetReinforcesTest(unittest.TestCase):
    def test_1(self):
        actual = alphabet_war_reinforces(["abcdefg", "hijklmn"], ["   *   ", "*  *   "])
        self.assertEqual(actual, 'hi___fg')

    def test_2(self):
        actual = alphabet_war_reinforces(["aaaaa", "bbbbb", "ccccc", "ddddd"], ["*", " *", "   "])
        self.assertEqual(actual, 'ccbaa')

    def test_3(self):
        reinforces = ["g964xxxxxxxx",
                      "myjinxin2015",
                      "steffenvogel",
                      "smile67xxxxx",
                      "giacomosorbi",
                      "freywarxxxxx",
                      "bkaesxxxxxxx",
                      "vadimbxxxxxx",
                      "zozofouchtra",
                      "colbydauphxx"]
        airstrikes = ["* *** ** ***",
                      " ** * * * **",
                      " * *** * ***",
                      " **  * * ** ",
                      "* ** *   ***",
                      "***   ",
                      "**",
                      "*",
                      "*"]
        actual = alphabet_war_reinforces(reinforces, airstrikes)
        self.assertEqual(actual, 'codewarsxxxx', 'Top 50 massacre failure')


if __name__ == '__main__':
    unittest.main()
