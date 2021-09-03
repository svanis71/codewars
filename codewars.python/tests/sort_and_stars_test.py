import unittest

from sort_and_stars import two_sort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(two_sort(["bitcoin", "take", "over", "the", "world", "maybe", "who", "knows", "perhaps"]),
                         'b***i***t***c***o***i***n')
        self.assertEqual(two_sort(
            ["turns", "out", "random", "test", "cases", "are", "easier", "than", "writing", "out", "basic", "ones"]),
            'a***r***e')
        self.assertEqual(two_sort(["lets", "talk", "about", "javascript", "the", "best", "language"]),
                         'a***b***o***u***t')
        self.assertEqual(two_sort(["i", "want", "to", "travel", "the", "world", "writing", "code", "one", "day"]),
                         'c***o***d***e')
        self.assertEqual(two_sort(["Lets", "all", "go", "on", "holiday", "somewhere", "very", "cold"]),
                         'L***e***t***s')


if __name__ == '__main__':
    unittest.main()
