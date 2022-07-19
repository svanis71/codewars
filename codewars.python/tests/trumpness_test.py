import unittest

from trumpness_detect import trump_detector


class TrumpnessTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, trump_detector("I will build a huge wall"), 'Zero trumpness')

    def test_2(self):
        self.assertEqual(4, trump_detector("HUUUUUGEEEE WAAAAAALL"), 'Trumpness factor 4')

    def test_4(self):
        self.assertEqual(2.5, trump_detector("MEXICAAAAAAAANS GOOOO HOOOMEEEE"), 'Trumpness factor 2,5')

    def test_5(self):
        self.assertEqual(1.89, trump_detector("America NUUUUUKEEEE Oooobaaaamaaaaa"), 'Trumpness factor 1,89')

    def test_6(self):
        self.assertEqual(1.56, trump_detector("listen migrants: IIII KIIIDD YOOOUUU NOOOOOOTTT"),
                         'Trumpness factor 1,56')

    def test_7(self):
        self.assertEqual(0.89, trump_detector('I kiiiid you not! Buuiild: traadiiiiition I AM TELLING THE TRUTH MIGRANTS. I haaaaaveeeee long fingers, HUGE truuump, GO HOME, baaaad foooreigners!!! Faaamiily I HAVE LONG FINGERS succeeess, MIGRANTS!!!!!!1!! Ameeeeriiica faamiiiiily nauuughty countries!!! Truuump uuniversity preeeeetty wiiife. Boombs, GOOD AMERICANS NUKE boordeeeer!!! Booooordeeeeer: preeeeetty wiife... Buuuiild!!! Eeeeexceeeellent sons pretty wiiife BUILD... Goo hoooome: I kiid yooooou not, I knoow iit!!!!!!!1!!'))

    def test_8(self):
        self.assertEqual(0.87, trump_detector('I AM TELLING THE TRUTH BOOOOOMBS: nuuuuuukeee, mexiiicans... MIGRANTS... Truuuuump!?! HUGE. I aaam teelling the truth!!!?!?!?!?!'))



if __name__ == '__main__':
    unittest.main()
