import unittest

from parameterized import parameterized

from kyu6.last_non_empty import last_non_empty_string


class MyTestCase(unittest.TestCase):
    @parameterized.expand([('aabcbbca', 'ba'),
                           ('abcd', 'abcd'),
                           ('zzxdccvzdd', 'zd')])
    def test_string(self, string: str, expected_result: str) -> None:
        self.assertEqual(expected_result, last_non_empty_string(string))


if __name__ == '__main__':
    unittest.main()
