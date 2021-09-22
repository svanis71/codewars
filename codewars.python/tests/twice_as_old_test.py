import unittest
from twice_as_old import twice_as_old


class MyTestCase(unittest.TestCase):
    def test_fixture(self):
        self.assertEqual(twice_as_old(36,7) , 22)
        self.assertEqual(twice_as_old(55,30) , 5)
        self.assertEqual(twice_as_old(42,21) , 0)
        self.assertEqual(twice_as_old(22,1) , 20)
        self.assertEqual(twice_as_old(29,0) , 29)