#!/usr/bin/env python
import unittest
from minesweep import MineSweeper


class TestMineSweeper(unittest.TestCase):

    def setUp(self):
        pass

    def test_game_object_is_created_properly(self):
        rows = 4
        cols = 5
        game = MineSweeper(rows, cols)
        self.assertIsNotNone(game)
        self.assertEquals(game.rowSize, rows)
        self.assertEquals(game.colSize, cols)

    def test_board_returns_correctly(self):
        rows = 8
        cols = 4
        game = MineSweeper(rows, cols)
        self.assertIsNotNone(game)
        board = game.board()
        self.assertIsNotNone(board)

if __name__ == '__main__':
    unittest.main()
