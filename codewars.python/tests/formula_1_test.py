import unittest

from formula_1 import champion_rank


class FormulaOneTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(champion_rank(3, ""), 3)
        self.assertEqual(champion_rank(12, "4 O 3 O"), 12)
        self.assertEqual(champion_rank(10, "1 I 10 O 2 I"), 7)

    def test_2(self):
        self.assertEqual(champion_rank(17, "2 O 17 I"), -1)

    def test_3(self):
        self.assertEqual(champion_rank(2,
                                       "9 O 17 O 9 O 12 O 2 O 12 O 9 O 1 O 5 O 12 O 17 O 20 O 16 O 7 O 2 O 8 O 16 O 14 O 3 O 14 O 11 O 16 O 1 O 13 O 8 O 14 O 5 O 12 O 4 O"),
                         1)


if __name__ == '__main__':
    unittest.main()
