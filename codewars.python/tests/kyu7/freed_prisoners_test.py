import unittest

from parameterized import parameterized

from kyu7.freed_prisoners import freed_prisoners


class MyTestCase(unittest.TestCase):
    @parameterized.expand([
        ([True, True, False, False, False, True, False], 4),
        ([True, False, False, False, False, False, False], 2),
        ([True, True, True, False, False, False], 2),
        ([True, False, True, False, True, False], 6),
        ([True, True, True], 1),
        ([False, False, False], 0),
        ([False, True, True, True], 0)
    ])
    def test_something(self, prisoners: list[bool], expected: int):
        self.assertEqual(expected, freed_prisoners(prisoners))


if __name__ == '__main__':
    unittest.main()
