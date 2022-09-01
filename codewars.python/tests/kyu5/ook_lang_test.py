import unittest

from kyu5.ook_lang import okkOokOo


class OokLangTests(unittest.TestCase):
    def test_h(self):
        self.assertEqual(okkOokOo('Ok, Ook, Ooo!'), 'H')

    def test_e(self):
        self.assertEqual(okkOokOo('Okk, Ook, Ok!'), 'e')

    def test_l(self):
        self.assertEqual(okkOokOo('Okk, Okk, Oo!'), 'l')

    def test_o(self):
        self.assertEqual(okkOokOo('Okk, Okkkk!'), 'o')

    def test_atuin(self):
        self.assertEqual("A'Tuin", okkOokOo(
            'Ok, Oooook?  Ok, Ookkk?  Ok, Ok, Ok, Oo?  Okkk, Ok, Ok?  Okk, Ok, Ook?  Okk, Okkk, O!'))

    def test_ankhmorpork(self):
        self.assertEqual("Ankh-Morpork", okkOokOo(
            'Ok, Oooook?  Okk, Okkk, O?  Okk, Ok, Okk?  Okk, Ok, Ooo?  Ok, Okk, Ok?  Ok, Ookk, Ok?  Okk, Okkkk?  Okkk, Ook, O?  Okkk, Oooo?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Ok, Okk!'))

    def test_sirterry(self):
        self.assertEqual("AT LAST, SIR TERRY, WE MUST WALK TOGETHER", okkOokOo(
            'Ok, Oooook?  Ok, Ok, Ok, Oo?  Ok, Ooooo?  Ok, Ookk, Oo?  Ok, Oooook?  Ok, Ok, Ookk?  Ok, Ok, Ok, Oo?  Ook, Okk, Oo?  Ok, Ooooo?  Ok, Ok, Ookk?  Ok, Ook, Ook?  Ok, Ok, Ook, O?  Ok, Ooooo?  Ok, Ok, Ok, Oo?  Ok, Oook, Ok?  Ok, Ok, Ook, O?  Ok, Ok, Ook, O?  Ok, Okk, Ook?  Ook, Okk, Oo?  Ok, Ooooo?  Ok, Ok, Okkk?  Ok, Oook, Ok?  Ok, Ooooo?  Ok, Ookk, Ok?  Ok, Ok, Ok, Ok?  Ok, Ok, Ookk?  Ok, Ok, Ok, Oo?  Ok, Ooooo?  Ok, Ok, Okkk?  Ok, Oooook?  Ok, Ookk, Oo?  Ok, Ook, Okk?  Ok, Ooooo?  Ok, Ok, Ok, Oo?  Ok, Ookkkk?  Ok, Oookkk?  Ok, Oook, Ok?  Ok, Ok, Ok, Oo?  Ok, Ook, Ooo?  Ok, Oook, Ok?  Ok, Ok, Ook, O!'))

    def test_berilia(self):
        self.assertEqual("Berilia", okkOokOo('Ok, Ooook, O?  '
                                             'Okk, Ook, Ok?  '
                                             'Okkk, Ook, O?  '
                                             'Okk, Ok, Ook?  '
                                             'Okk, Okk, Oo?  '
                                             'Okk, Ok, Ook?  '
                                             'Okk, Ooook!'))

    def test_jeraken(self):
        self.assertEqual("Jerakeen",
                         okkOokOo('Ok, Ook, Ok, O?  '
                                  'Okk, Ook, Ok?  '
                                  'Okkk, Ook, O?  '
                                  'Okk, Ooook?  '
                                  'Okk, Ok, Okk?  '
                                  'Okk, Ook, Ok?  '
                                  'Okk, Ook, Ok?  '
                                  'Okk, Okkk, O!'))

    def test_hello(self):
        self.assertEqual(okkOokOo('Ok, Ook, Ooo? Okk, Ook, Ok? Okk, Okk, Oo? Okk, Okk, Oo? Okk, Okkkk!'), 'Hello')

    def test_helloworld(self):
        self.assertEqual('Hello World!', okkOokOo(
            'Ok, Ook, Ooo?  Okk, Ook, Ok?  Okk, Okk, Oo?  Okk, Okk, Oo?  Okk, Okkkk?  Ok, Ooooo?  Ok, Ok, Okkk?  Okk, Okkkk?  Okkk, Ook, O?  Okk, Okk, Oo?  Okk, Ook, Oo?  Ook, Ooook!'))

    def test_tphon(self):
        self.assertEqual("T'Phon", okkOokOo(
            'Ok, Ok, Ok, Oo?  '
            'Ok, Ookkk?  '
            'Ok, Ok, Oooo?  '
            'Okk, Ok, Ooo?  '
            'Okk, Okkkk?  '
            'Okk, Okkk, O!'))


if __name__ == '__main__':
    unittest.main()
