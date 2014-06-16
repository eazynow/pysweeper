#!/usr/bin/env python


class PySweeper(object):
    TILE_HIDDEN = "."
    TILE_CLEAR = " "
    TILE_MINE = "X"

    def __init__(self, rows=8, cols=8):
        self.mines = []
        self.rows = rows
        self.cols = cols

    def board(self):
        theboard = []
        for rowindex in range(0, self.rows):
            row = ""
            for colindex in range(0, self.cols):
                row = row + PySweeper.TILE_HIDDEN
            theboard.append(row)
        return theboard
