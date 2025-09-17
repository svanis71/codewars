import unittest
from datetime import datetime, timezone

from kyu5.mongoid import Mongo


class MyTestCase(unittest.TestCase):
    def test_isvalid(self):
        self.assertEqual(Mongo.is_valid(False), False)
        self.assertEqual(Mongo.is_valid([]), False)
        self.assertEqual(Mongo.is_valid(1234), False)
        self.assertEqual(Mongo.is_valid('123476sd'), False)
        self.assertEqual(Mongo.is_valid('507f1f77bcf86cd79943901'), False)
        self.assertEqual(Mongo.is_valid('507f1f77bcf86cd799439016'), True)

    def test_timestamp(self):
        self.assertEqual(Mongo.get_timestamp(False), False)
        self.assertEqual(Mongo.get_timestamp([]), False)
        self.assertEqual(Mongo.get_timestamp(1234), False)
        self.assertEqual(Mongo.get_timestamp('123476sd'), False)
        self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd79943901'), False)
        self.assertEqual(Mongo.get_timestamp('507f1f77bcf86cd799439016'),
                         datetime(2012, 10, 17, 21, 13, 27, tzinfo=timezone.utc))
        self.assertEqual(Mongo.get_timestamp('d07f1f77bcf86FF799439016'), False)


if __name__ == '__main__':
    unittest.main()
