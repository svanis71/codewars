import unittest
from digital_root import digital_root

class MyTestCase(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(digital_root(16), 7)

    def testcase2(self):
        self.assertEqual(digital_root(942), 6)

    def testcase3(self):
        self.assertEqual(digital_root(132189), 6)

    def testcase4(self):
        self.assertEqual(digital_root(493193), 2)

if __name__ == '__main__':
    unittest.main()
