import unittest

from reverse_words import reverse_words


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual('olleH', reverse_words('Hello'))

    def test_1(self):
        self.assertEqual(reverse_words('The quick brown fox jumps over the lazy dog.'),
                         'ehT kciuq nworb xof spmuj revo eht yzal .god')

    def test_2(self):
        self.assertEqual(reverse_words('apple'), 'elppa')

    def test_3(self):
        self.assertEqual(reverse_words('a b c d'), 'a b c d')

    def test_4(self):
        self.assertEqual(reverse_words('double  spaced  words'), 'elbuod  decaps  sdrow')


if __name__ == '__main__':
    unittest.main()
