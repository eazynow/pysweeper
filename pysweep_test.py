#!/usr/bin/env python
import unittest
from pysweep import PySweeper


class TestPySweeper(unittest.TestCase):

    def setUp(self):
        pass

    def test_game_object_is_created_properly(self):
        rows = 4
        cols = 5
        game = PySweeper(rows, cols)
        self.assertIsNotNone(game)
        self.assertEquals(game.rows, rows)
        self.assertEquals(game.cols, cols)

    def test_board_returns_correctly(self):
        rows = 8
        cols = 4
        game = PySweeper(rows, cols)
        self.assertIsNotNone(game)
        board = game.board()
        self.assertIsNotNone(board)

    def test_board_has_correct_rows(self):
        rows = 8
        cols = 4
        game = PySweeper(rows, cols)
        self.assertIsNotNone(game)
        board = game.board()
        self.assertIsNotNone(board)
        self.assertEquals(len(board), rows)

    def test_board_has_correct_cols(self):
        rows = 8
        cols = 8
        hidden_tile = "."
        game = PySweeper(rows, cols)
        self.assertIsNotNone(game)
        board = game.board()
        self.assertIsNotNone(board)
        for row in board:
            self.assertEquals(len(row), cols)
            for cell in row:
                self.assertEquals(hidden_tile, cell)

if __name__ == '__main__':
    unittest.main()
