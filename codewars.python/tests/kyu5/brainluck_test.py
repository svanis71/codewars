import unittest

from kyu5.brainluck import brain_luck


class BrainLuckTest(unittest.TestCase):
    def test_1(self):
        self.assertEqual(brain_luck(',+[-.,+]', 'Codewars' + chr(255)), 'Codewars')

    def test_2(self):
        # Echo until byte(0) encountered
        self.assertEqual(brain_luck(',[.[-],]', 'Codewars' + chr(0)), 'Codewars')

    def test_3(self):
        # Two numbers multiplier
        self.assertEqual(brain_luck(',>,<[>[->+>+<<]>>[-<<+>>]<<<-]>>.', chr(8) + chr(9)), chr(72))


if __name__ == '__main__':
    unittest.main()
