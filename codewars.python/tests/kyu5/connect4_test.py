import unittest
from unittest import TestCase

from kyu5.connect4 import Connect4


class TestConnect4(TestCase):
    def test_play1(self):
        game = Connect4()
        self.assertEqual(game.play(0), "Player 1 has a turn")
        self.assertEqual(game.play(0), "Player 2 has a turn")

    def test_play2(self):
        game = Connect4()
        self.assertEqual(game.play(0), "Player 1 has a turn")
        self.assertEqual(game.play(1), "Player 2 has a turn")
        self.assertEqual(game.play(0), "Player 1 has a turn")
        self.assertEqual(game.play(1), "Player 2 has a turn")
        self.assertEqual(game.play(0), "Player 1 has a turn")
        self.assertEqual(game.play(1), "Player 2 has a turn")
        self.assertEqual(game.play(0), "Player 1 wins!")

    def test_play3(self):
        game = Connect4()
        self.assertEqual(game.play(4), "Player 1 has a turn")
        self.assertEqual(game.play(4), "Player 2 has a turn")
        self.assertEqual(game.play(4), "Player 1 has a turn")
        self.assertEqual(game.play(4), "Player 2 has a turn")
        self.assertEqual(game.play(4), "Player 1 has a turn")
        self.assertEqual(game.play(4), "Player 2 has a turn")
        self.assertEqual(game.play(4), "Column full!")

    def test_play4(self):
        game = Connect4()
        self.assertEqual(game.play(1), "Player 1 has a turn")
        self.assertEqual(game.play(1), "Player 2 has a turn")
        self.assertEqual(game.play(2), "Player 1 has a turn")
        self.assertEqual(game.play(2), "Player 2 has a turn")
        self.assertEqual(game.play(3), "Player 1 has a turn")
        self.assertEqual(game.play(3), "Player 2 has a turn")
        self.assertEqual(game.play(4), "Player 1 wins!")
        self.assertEqual(game.play(4), "Game has finished!")

    def test_diagonal_left(self):
        game = Connect4()
        game.play(3)
        game.play(4)
        game.play(4)
        game.play(6)
        game.play(5)
        game.play(5)
        game.play(5)
        game.play(6)
        game.play(6)
        game.play(2)
        self.assertEqual(game.play(6), "Player 1 wins!")

    def test_diagonal_right(self):
        game = Connect4()
        game.play(0)
        game.play(1)
        game.play(2)
        game.play(0)
        game.play(3)
        game.play(0)
        game.play(2)
        game.play(1)
        game.play(1)
        game.play(4)
        self.assertEqual(game.play(0), "Player 1 wins!")

    def test_diagonal_right_again(self):
        game = Connect4()
        game.play(0)
        game.play(6)
        game.play(5)
        game.play(5)
        game.play(4)
        game.play(4)
        game.play(0)
        game.play(4)
        game.play(3)
        game.play(3)
        game.play(3)
        self.assertEqual(game.play(3), "Player 2 wins!")

    def test_vertical(self):
        game = Connect4()
        game.play(0)
        game.play(6)
        game.play(6)
        game.play(6)
        game.play(0)
        game.play(6)
        game.play(1)
        game.play(6)
        game.play(1)
        self.assertEqual(game.play(6), "Player 2 wins!")


if __name__ == '__main__':
    unittest.main()
