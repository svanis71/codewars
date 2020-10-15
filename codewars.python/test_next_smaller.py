import unittest

from next_smaller import next_smaller


class MyTestCase(unittest.TestCase):
    @unittest.skip
    def test_next_smaller_1(self):
        self.assertEqual(-1, next_smaller(3))

    def test_next_smaller_2(self):
        self.assertEqual(next_smaller(907), 790)

    @unittest.skip
    def test_next_smaller_3(self):
        self.assertEqual(next_smaller(531), 513)

    @unittest.skip
    def test_next_smaller_4(self):
        self.assertEqual(next_smaller(511), 151)

    @unittest.skip
    def test_next_smaller_5(self):
        self.assertEqual(next_smaller(135), -1)

    @unittest.skip
    def test_next_smaller_6(self):
        self.assertEqual(next_smaller(2071), 2017)

    @unittest.skip
    def test_next_smaller_7(self):
        self.assertEqual(next_smaller(414), 144)

    @unittest.skip
    def test_next_smaller_8(self):
        self.assertEqual(next_smaller(123456798), 123456789)

    def test_next_smaller_9(self):
        self.assertEqual(next_smaller(123456789), -1)

    @unittest.skip
    def test_next_smaller_10(self):
        self.assertEqual(next_smaller(1234567908), 1234567890)


if __name__ == '__main__':
    unittest.main()
