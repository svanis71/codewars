import unittest

from kyu6.last_digit_fibonacci import last_fib_digit


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(1, last_fib_digit(1))

    def test_21(self):
        self.assertEqual(6, last_fib_digit(21))

    def test_302(self):
        self.assertEqual(1, last_fib_digit(302))

    def test_4003(self):
        self.assertEqual(7, last_fib_digit(4003))

    def test_50004(self):
        self.assertEqual(8, last_fib_digit(50004))

    def test_600005(self):
        self.assertEqual(5, last_fib_digit(600005))

    def test_7000006(self):
        self.assertEqual(3, last_fib_digit(7000006))

    def test_80000007(self):
        self.assertEqual(8, last_fib_digit(80000007))

    def test_900000008(self):
        self.assertEqual(1, last_fib_digit(900000008))

    def test_bignum1(self):
        self.assertEqual(0, last_fib_digit(8938091204004396511347240))

    def test_bignum2(self):
        self.assertEqual(0, last_fib_digit(4595935748985531770145960))


if __name__ == '__main__':
    unittest.main()
