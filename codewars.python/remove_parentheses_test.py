import unittest
from re import sub


def remove_parentheses(s):
    return s if s.find('(') < 0 else remove_parentheses(sub(r'\([\w\s]*\)', '', s))
    # rs = sub(r'\([\w\s]*\)', '', s)
    # while rs.find('(') >= 0:
    #     rs = sub(r'\([\w\s]*\)', '', rs)
    # return rs

class MyTestCase(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(remove_parentheses(''), '')

    def test_lots_of_spaces(self):
        self.assertEqual(remove_parentheses('   '), '   ')

    def test_basic(self):
        self.assertEqual(remove_parentheses('aa(bb)bb'), 'aabb')

    def test_with_space(self):
        self.assertEqual(remove_parentheses('aa (bb cc) bb'), 'aa  bb')

    def test_nested(self):
        self.assertEqual(remove_parentheses('aa (bb (cc) dd) bb'), 'aa  bb')

    def test_multiple_groups(self):
        self.assertEqual(remove_parentheses('(first group) (second group) (third group)'), '  ')


if __name__ == '__main__':
    unittest.main()
