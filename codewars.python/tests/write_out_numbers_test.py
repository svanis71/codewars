import unittest

'''
https://www.codewars.com/kata/52724507b149fa120600031d/train/python
'''
numbers = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine',
           10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen',
           17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty',
           60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 100: 'hundred', 1000: 'thousand'}


def number2words(n):
    if n < 21:
        return numbers[n]
    l, s = [], ''
    while n > 0:
        n, remain = divmod(n, 10)
        l.append(remain)
    for i, n in enumerate(l):
        pass
    return s


class MyTestCase(unittest.TestCase):
    def test_low(self):
        self.assertEqual(number2words(0), "zero")
        self.assertEqual(number2words(1), "one")
        self.assertEqual(number2words(8), "eight")

    def test_tens(self):
        self.assertEqual(number2words(10), "ten")
        self.assertEqual(number2words(19), "nineteen")
        self.assertEqual(number2words(20), "twenty")
        self.assertEqual(number2words(22), "twenty-two")
    #     self.assertEqual(number2words(54), "fifty-four")
    #     self.assertEqual(number2words(80), "eighty")
    #     self.assertEqual(number2words(98), "ninety-eight")
    #
    # def test_hundreds(self):
    #     self.assertEqual(number2words(100), "one hundred")
    #     self.assertEqual(number2words(301), "three hundred one")
    #     self.assertEqual(number2words(793), "seven hundred ninety-three")
    #     self.assertEqual(number2words(800), "eight hundred")
    #     self.assertEqual(number2words(650), "six hundred fifty")
    #
    # def test_thounsands(self):
    #     self.assertEqual(number2words(1000), "one thousand")
    #     self.assertEqual(number2words(1003), "one thousand three")
    #     self.assertEqual(number2words(3051), "three thousand fifty-one")
    #     self.assertEqual(number2words(7200), "seven thousand two hundred")
    #     self.assertEqual(number2words(7219), "seven thousand two hundred nineteen")
    #     self.assertEqual(number2words(8330), "eight thousand three hundred thirty")
    #     self.assertEqual(number2words(99999), "ninety-nine thousand nine hundred ninety-nine")
    #     self.assertEqual(number2words(888888), "eight hundred eighty-eight thousand eight hundred eighty-eight")


if __name__ == '__main__':
    unittest.main()
