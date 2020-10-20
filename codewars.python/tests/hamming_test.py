import unittest
from hamming import hamming


class MyTestCase(unittest.TestCase):
    def test_hamming1(self):
        self.assertEqual(hamming(1), 1, "hamming(1) should be 1")

    def test_hamming2(self):
        self.assertEqual(hamming(2), 2, "hamming(2) should be 2")

    def test_hamming3(self):
        self.assertEqual(hamming(3), 3, "hamming(3) should be 3")

    def test_hamming4(self):
        self.assertEqual(hamming(4), 4, "hamming(4) should be 4")

    def test_hamming5(self):
        self.assertEqual(hamming(5), 5, "hamming(5) should be 5")

    def test_hammin6(self):
        self.assertEqual(hamming(6), 6, "hamming(6) should be 6")

    def test_hammin7(self):
        self.assertEqual(hamming(7), 8, "hamming(7) should be 8")

    def test_hammin8(self):
        self.assertEqual(hamming(8), 9, "hamming(8) should be 9")

    def test_hammin9(self):
        self.assertEqual(hamming(9), 10, "hamming(9) should be 10")

    def test_hamming10(self):
        self.assertEqual(hamming(10), 12, "hamming(10) should be 12")

    def test_hamming11(self):
        self.assertEqual(hamming(11), 15, "hamming(11) should be 15")

    def test_hamming12(self):
        self.assertEqual(hamming(12), 16, "hamming(12) should be 16")

    def test_hamming13(self):
        self.assertEqual(hamming(13), 18, "hamming(13) should be 18")

    def test_hamming14(self):
        self.assertEqual(hamming(14), 20, "hamming(14) should be 20")

    def test_hamming15(self):
        self.assertEqual(hamming(15), 24, "hamming(15) should be 24")

    def test_hamming16(self):
        self.assertEqual(hamming(16), 25, "hamming(16) should be 25")

    def test_hamming17(self):
        self.assertEqual(hamming(17), 27, "hamming(17) should be 27")

    def test_hamming18(self):
        self.assertEqual(hamming(18), 30, "hamming(18) should be 30")

    def test_hamming19(self):
        self.assertEqual(hamming(19), 32, "hamming(19) should be 32")


if __name__ == '__main__':
    unittest.main()
