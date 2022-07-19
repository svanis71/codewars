import unittest

from remove_parentheses import remove_parentheses


class RemoveParenthesesTests(unittest.TestCase):
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
