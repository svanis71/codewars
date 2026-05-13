import unittest

from parameterized import parameterized

from kyu6.morse_code import decode_morse


class MyTestCase(unittest.TestCase):
    @parameterized.expand([('.... . -.--   .--- ..- -.. .', 'HEY JUDE'),
                           ('.-', 'A'),
                           ('--...', '7'),
                           ('...-..-', '$'),
                           ('.', 'E'),
                           ('..', 'I'),
                           ('. .', 'EE'),
                           ('.   .', 'E E'),
                           ('...-..- ...-..- ...-..-', '$$$'),
                           ('----- .---- ..--- ---.. ----.', '01289'),
                           ('.-... ---...   -..-. --...', '&: /7'),
                           ('...---...', 'SOS'),
                           ('... --- ...', 'SOS'),
                           ('...   ---   ...', 'S O S'),
                           (' . ', 'E'),
                           ('   .   . ', 'E E')
                           ])
    def test_morse_codes(self, morse_code: str, expected: str):
        self.assertEqual(decode_morse(morse_code), expected)

    def test_morse_complex_example(self):
        self.assertEqual(decode_morse(
            '      ...---... -.-.--   - .... .   --.- ..- .. -.-. -.-   -... .-. --- .-- -.   ..-. --- -..-   .--- ..- -- .--. ...   --- ...- . .-.   - .... .   .-.. .- --.. -.--   -.. --- --. .-.-.-  '),
            'SOS! THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG.')

    if __name__ == '__main__':
        unittest.main()
