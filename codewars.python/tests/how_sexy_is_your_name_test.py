import unittest

from how_sexy_is_your_name import sexy_name


class SexyNameTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(sexy_name('GUV'), 'NOT TOO SEXY')
        self.assertEqual(sexy_name('PHUG'), "NOT TOO SEXY")
        self.assertEqual(sexy_name('FFFFF'), 'NOT TOO SEXY')
        self.assertEqual(sexy_name(''), "NOT TOO SEXY")
        self.assertEqual(sexy_name('PHUG'), "NOT TOO SEXY")
        self.assertEqual(sexy_name('BOB'), "PRETTY SEXY")
        self.assertEqual(sexy_name('JLJ'), 'PRETTY SEXY')
        self.assertEqual(sexy_name('HHHHHU'), 'PRETTY SEXY')
        self.assertEqual(sexy_name('BOB'), "PRETTY SEXY")
        self.assertEqual(sexy_name('WWWWWU'), "PRETTY SEXY")
        self.assertEqual(sexy_name('YOU'), 'VERY SEXY')
        self.assertEqual(sexy_name('FABIO'), "VERY SEXY")
        self.assertEqual(sexy_name('ARUUUUUUUUU'), 'VERY SEXY')
        self.assertEqual(sexy_name('ROBBY'), 'THE ULTIMATE SEXIEST')
        self.assertEqual(sexy_name('SAMANTHA'), 'THE ULTIMATE SEXIEST')
        self.assertEqual(sexy_name('DONALD TRUMP'), "THE ULTIMATE SEXIEST")
        self.assertEqual(sexy_name('BILL GATES'), "THE ULTIMATE SEXIEST")
        self.assertEqual(sexy_name('SCARLETT JOHANSSON'), "THE ULTIMATE SEXIEST")
        self.assertEqual(sexy_name('CODEWARS'), "THE ULTIMATE SEXIEST")
        self.assertEqual(sexy_name('PAMELA ANDERSON'), "THE ULTIMATE SEXIEST")
        self.assertEqual(sexy_name('you'), 'VERY SEXY')
        self.assertEqual(sexy_name('Codewars'), "THE ULTIMATE SEXIEST")


if __name__ == '__main__':
    unittest.main()
