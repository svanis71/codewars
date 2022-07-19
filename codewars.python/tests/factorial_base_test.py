import unittest

from factorial_base import dec_2_fact_string, fact_string_2_dec


class FactorialBaseTests(unittest.TestCase):
    def test_something(self):
        self.assertEqual(dec_2_fact_string(463), "341010")
        self.assertEqual(dec_2_fact_string(2982), "4041000")

    def fact_2_dec(self):
        self.assertEqual(fact_string_2_dec("341010"), 463)
        self.assertEqual(fact_string_2_dec("4042100"), 2990)


if __name__ == '__main__':
    unittest.main()
