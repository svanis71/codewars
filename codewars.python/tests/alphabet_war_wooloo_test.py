import unittest

from alphabet_war import alphabet_war_wooloo


class Alphabet_Wooloo_test(unittest.TestCase):
    def test(self):
        self.assertEqual(alphabet_war_wooloo("z"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("zm"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("zmq"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("tz"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("jbdt"), "Let's fight again!")
        self.assertEqual(alphabet_war_wooloo("jz"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("azt"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("wololooooo"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("ztztztzs"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("mdtjtms"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("besbjjw"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("zt"), "Left side wins!")
        self.assertEqual(alphabet_war_wooloo("sj"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("zdqmwpbs"), "Let's fight again!")
        self.assertEqual(alphabet_war_wooloo("tzj"), "Right side wins!")
        self.assertEqual(alphabet_war_wooloo("mmcjwtqdpzjsjbcpwzzzabmdb"), "Right side wins!")
