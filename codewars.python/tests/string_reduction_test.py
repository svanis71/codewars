import unittest

from string_reduction import reduce_string


class StringReductionTests(unittest.TestCase):
    def test_1(self):
        self.assertEqual(0, reduce_string("xyz", "yxz"))

    def test_2(self):
        self.assertEqual(2, reduce_string("abcxyz", "ayxz"))

    def test_3(self):
        self.assertEqual(5, reduce_string("abcdexyz", "yxz"))

    def test_4(self):
        self.assertEqual(0, reduce_string("xyz", "yxxz"))

    def test_5(self):
        self.assertEqual(0, reduce_string("abdegfg", "ffdb"))

    def test_6(self):
        self.assertEqual(5, reduce_string("aabcdefg", "fbd"))

    def test_7(self):
        self.assertEqual(5, reduce_string("aabcdefg", "fdb"))

    def test_4906178931487637470(self):
        self.assertEqual(18, reduce_string("wbokhddiifzbejqotnawxutf", "wbokhd"))

    def test_1436016228816704797(self):
        self.assertEqual(16, reduce_string("bptrrzysjsvbsbnmuiocp", "bptrr"))


if __name__ == '__main__':
    unittest.main()
