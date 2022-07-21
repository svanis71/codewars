import unittest

from paintfuck import interpreter


class PaintFuckTests(unittest.TestCase):
    def test_basic_1(self):
        self.assertEqual(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 0, 6, 9),
                         "000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000")

    def test_basic_2(self):
        self.assertEqual(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 7, 6, 9),
                         "111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000")

    def test_basic_3(self):
        self.assertEqual(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 19, 6, 9),
                         "111100\r\n000010\r\n000001\r\n000010\r\n000100\r\n000000\r\n000000\r\n000000\r\n000000")

    def test_basic_4(self):
        self.assertEqual(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 42, 6, 9),
                         "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000")

    def test_basic_5(self):
        self.assertEqual(interpreter("*e*e*e*es*es*ws*ws*w*w*w*n*n*n*ssss*s*s*s*", 100, 6, 9),
                         "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000")

    def test_ignore_invalido_instructions(self):
        code = 'o*e*eq*reqrqp*ppooqqeaqqsr*yqaooqqqfqarppppfffpppppygesfffffffffu*wrs*agwpffffst*w*uqrw*qyaprrrrrw*nuiiiid???ii*n*ynyy??ayd*r:rq????qq::tqaq:y???ss:rqsr?s*qs:q*?qs*tr??qst?q*r'
        expected = '111100\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000\r\n000000'
        self.assertEqual(expected, interpreter(code, 7, 6, 9))

    def test_fail(self):
        self.assertEqual(interpreter("sssss*s*s*s*s*www*w*w*seee*ee*s*w*sw*sw*eee*n*es*e*", 1000, 6, 9),
                         "111100\r\n100010\r\n100001\r\n100010\r\n111100\r\n100000\r\n100000\r\n100000\r\n100000")

    def test_loop(self):
        code = '*[es*]'
        expected = '01111\r\n11111\r\n11111\r\n11111\r\n11111\r\n11111'
        self.assertEqual(expected, interpreter(code, 1000, 5, 6))

    def test_nested_loop_9(self):
        code = '*[s[e]*]'
        expected = '10000\r\n10000\r\n10000\r\n00000\r\n00000'
        self.assertEqual(expected, interpreter(code, 9, 5, 5))

    def test_nested_loop_5(self):
        code = '*[s[e]*]'
        expected = '10000\r\n10000\r\n00000\r\n00000\r\n00000'
        self.assertEqual(expected, interpreter(code, 5, 5, 5))


if __name__ == '__main__':
    unittest.main()
