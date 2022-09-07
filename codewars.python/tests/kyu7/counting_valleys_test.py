import unittest

from kyu7.counting_valleys import counting_valleys


class MyTestCase(unittest.TestCase):
    def test_1(self):
        self.assertEqual(counting_valleys('UFFFD'), 0)

    def test_2(self):
        self.assertEqual(counting_valleys('DFFFD'), 0)

    def test_3(self):
        self.assertEqual(counting_valleys('UFFFU'), 0)

    def test_4(self):
        self.assertEqual(counting_valleys('DFFFU'), 1)

    def test_5(self):
        self.assertEqual(counting_valleys('UFFDDFDUDFUFU'), 1)

    def test_6(self):
        self.assertEqual(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFU'), 2)

    def test_7(self):
        self.assertEqual(counting_valleys('UFFDDFDUDFUFUUFFDDUFFDDUFFDDUDUDUDUDUDUUUUUUUUU'), 3)

    def test_8(self):
        self.assertEqual(counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 4)

    def test_9(self):
        self.assertEqual(
            counting_valleys('UFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFUUFFDDFDUDFUFU'), 6)


if __name__ == '__main__':
    unittest.main()
