import unittest

from parameterized import parameterized

from kyu5.card_game import card_game


class MyTestCase(unittest.TestCase):
    @parameterized.expand([(51, 6),
                           (10, 8),
                           (4, 3),
                           (5, 2),
                           (12, 9),
                           (100000000000, 99999999950)])
    def test_something(self, num_of_cards, expected_alice_max):
        self.assertEqual(expected_alice_max, card_game(num_of_cards))  # add assertion here


if __name__ == '__main__':
    unittest.main()
