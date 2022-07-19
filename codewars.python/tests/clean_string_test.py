import unittest

from clean_string import clean_string


class CleanStringTests(unittest.TestCase):
    def test_something(self):
        tests = [
            ('abc#d##c', "ac"),
            ('abc####d##c#', ""),
            ("#######", ""),
            ("", "")
        ]
        for tst, expected in tests:
            self.assertEqual(expected, clean_string(tst), f'{tst} expected {expected}')


if __name__ == '__main__':
    unittest.main()
