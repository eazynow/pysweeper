#!/usr/bin/env python


class PySweeper(object):
    def __init__(self, rows=8, cols=8):
        self.rows = []
        self.rowSize = rows
        self.colSize = cols

    def board(self):
        theboard = []
        for rowindex in range(0, self.rowSize):
            row = ""
            for colindex in range(0, self.colSize):
                row = row + "."
            theboard.append(row)
        return theboard
