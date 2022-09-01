import unittest

from kyu4.parseInt import parse_int


class MyTestCase(unittest.TestCase):
    def test_0(self):
        self.assertEqual(parse_int('zero'), 0)

    def test_1(self):
        self.assertEqual(parse_int('one'), 1)

    def test_2(self):
        self.assertEqual(parse_int('two'), 2)

    def test_3(self):
        self.assertEqual(parse_int('three'), 3)

    def test_4(self):
        self.assertEqual(parse_int('four'), 4)

    def test_5(self):
        self.assertEqual(parse_int('five'), 5)

    def test_6(self):
        self.assertEqual(parse_int('six'), 6)

    def test_7(self):
        self.assertEqual(parse_int('seven'), 7)

    def test_8(self):
        self.assertEqual(parse_int('eight'), 8)

    def test_9(self):
        self.assertEqual(parse_int('nine'), 9)

    def test_10(self):
        self.assertEqual(parse_int('ten'), 10)

    def test_20(self):
        self.assertEqual(parse_int('twenty'), 20)

    def test_21(self):
        self.assertEqual(parse_int('twenty-one'), 21)

    def test_37(self):
        self.assertEqual(parse_int('thirty-seven'), 37)

    def test_46(self):
        self.assertEqual(parse_int('forty-six'), 46)

    def test_59(self):
        self.assertEqual(parse_int('fifty-nine'), 59)

    def test_68(self):
        self.assertEqual(parse_int('sixty-eight'), 68)

    def test_72(self):
        self.assertEqual(parse_int('seventy-two'), 72)

    def test_83(self):
        self.assertEqual(parse_int('eighty-three'), 83)

    def test_94(self):
        self.assertEqual(parse_int('ninety-four'), 94)

    def test_100(self):
        self.assertEqual(parse_int('one hundred'), 100)

    def test_101(self):
        self.assertEqual(parse_int('one hundred one'), 101)

    def test_101_again(self):
        self.assertEqual(parse_int('one hundred and one'), 101)

    def test_169(self):
        self.assertEqual(parse_int('one hundred sixty-nine'), 169)

    def test_299(self):
        self.assertEqual(parse_int('two hundred and ninety-nine'), 299)

    def test_736(self):
        self.assertEqual(parse_int('seven hundred thirty-six'), 736)

    def test_2000(self):
        self.assertEqual(parse_int('two thousand'), 2000)

    def test_1337(self):
        self.assertEqual(parse_int('one thousand three hundred and thirty-seven'), 1337)

    def test_10000(self):
        self.assertEqual(parse_int('ten thousand'), 10000)

    def test_26359(self):
        self.assertEqual(parse_int('twenty-six thousand three hundred and fifty-nine'), 26359)

    def test_35000(self):
        self.assertEqual(parse_int('thirty-five thousand'), 35000)

    def test_99999(self):
        self.assertEqual(parse_int('ninety-nine thousand nine hundred and ninety-nine'), 99999)

    def test_666666(self):
        self.assertEqual(parse_int('six hundred sixty-six thousand six hundred sixty-six'), 666666)

    def test_700000(self):
        self.assertEqual(parse_int('seven hundred thousand'), 700000)

    def test_200003(self):
        self.assertEqual(parse_int('two hundred thousand three'), 200003)

    def test_200003_again(self):
        self.assertEqual(parse_int('two hundred thousand and three'), 200003)

    def test_203000(self):
        self.assertEqual(parse_int('two hundred three thousand'), 203000)

    def test_500300(self):
        self.assertEqual(parse_int('five hundred thousand three hundred'), 500300)

    def test_888888(self):
        self.assertEqual(parse_int('eight hundred eighty-eight thousand eight hundred and eighty-eight'), 888888)

    def test_1M(self):
        self.assertEqual(parse_int('one million'), 1000000)


if __name__ == '__main__':
    unittest.main()
