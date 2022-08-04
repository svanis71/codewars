import unittest

from int4toipv4 import int32_to_ip


class IntToIpv4_Tests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(int32_to_ip(2154959208), "128.114.17.104")
        self.assertEqual(int32_to_ip(0), "0.0.0.0")
        self.assertEqual(int32_to_ip(2149583361), "128.32.10.1")


if __name__ == '__main__':
    unittest.main()
