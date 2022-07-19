import unittest

from alphabet_war import alphabet_war_nuclear


class AlphabetWarNuclear(unittest.TestCase):
    def test_1(self):
        self.assertEqual(alphabet_war_nuclear('[a]#[b]#[c]'), 'ac')

    def test_2(self):
        self.assertEqual(alphabet_war_nuclear('[a]#b#[c][d]'), 'd')

    def test_3(self):
        self.assertEqual(alphabet_war_nuclear('[a][b][c]'), 'abc')

    def test_4(self):
        self.assertEqual(alphabet_war_nuclear('##a[a]b[c]#'), 'c')

    def test_5(self):
        self.assertEqual(alphabet_war_nuclear('abde[fgh]ijk'), 'abdefghijk')

    def test_6(self):
        self.assertEqual(alphabet_war_nuclear('ab#de[fgh]ijk'), 'fgh')

    def test_7(self):
        self.assertEqual(alphabet_war_nuclear('ab#de[fgh]ij#k'), '')

    def test_8(self):
        self.assertEqual(alphabet_war_nuclear('##abde[fgh]ijk'), '')

    def test_9(self):
        self.assertEqual(alphabet_war_nuclear('##abde[fgh]'), '')

    def test_10(self):
        self.assertEqual(alphabet_war_nuclear('##abcde[fgh]'), '')

    def test_11(self):
        self.assertEqual(alphabet_war_nuclear('abcde[fgh]'), 'abcdefgh')

    def test_12(self):
        self.assertEqual(alphabet_war_nuclear('##abde[fgh]ijk[mn]op'), 'mn')

    def test_13(self):
        self.assertEqual(alphabet_war_nuclear('#abde[fgh]i#jk[mn]op'), 'mn')

    def test_14(self):
        self.assertEqual(alphabet_war_nuclear('[ab]adfd[dd]##[abe]dedf[ijk]d#d[h]#'), 'abijk')


if __name__ == '__main__':
    unittest.main()
