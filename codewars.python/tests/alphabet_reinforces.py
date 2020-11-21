import unittest

from alphabet_war import alphabet_war_reinforces


class AlphabetReinforcesTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(alphabet_war_reinforces(["abcdefg", "hijklmn"], ["   *   ", "*  *   "]), 'hi___fg');

    def test_2(self):
        self.assertEqual(alphabet_war_reinforces(["aaaaa", "bbbbb", "ccccc", "ddddd"], ["*", " *", "   "]), 'ccbaa');

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
        self.assertEqual(alphabet_war_reinforces(reinforces, airstrikes), 'codewarsxxxx', 'Top 50 massacre failure');


if __name__ == '__main__':
    unittest.main()
