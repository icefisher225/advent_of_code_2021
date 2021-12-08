import os, sys, time, math

class Board:
    def __init__(self, grid):
        self._00 = grid[0][0]
        self._01 = grid[0][1]
        self._02 = grid[0][2]
        self._03 = grid[0][3]
        self._04 = grid[0][4]
        self._10 = grid[1][0]
        self._11 = grid[1][1]
        self._12 = grid[1][2]
        self._13 = grid[1][3]
        self._14 = grid[1][4]
        self._20 = grid[2][0]
        self._21 = grid[2][1]
        self._22 = grid[2][2]
        self._23 = grid[2][3]
        self._24 = grid[2][4]
        self._30 = grid[3][0]
        self._31 = grid[3][1]
        self._32 = grid[3][2]
        self._33 = grid[3][3]
        self._34 = grid[3][4]
        self._40 = grid[4][0]
        self._41 = grid[4][1]
        self._42 = grid[4][2]
        self._43 = grid[4][3]
        self._44 = grid[4][4]

    def rows(self, row):
        rs = list()
        rs2 = list()
        for i in range(5):
            rs.append(eval(f"self._{row}{i}"))
        return rs

    def cols(self, col):
        rs = list()
        rs2 = list()
        for i in range(5):
            rs.append(eval(f"self._{i}{col}"))
        return rs

    def diags(self):
        rs = list()
        rs2 = list()
        for i in range(5):
            rs.append(eval(f"self._{i}{i}"))
        for i in range(5):
            rs2.append(eval(f"self._{(4-i)}{i}"))
        return (rs, rs2)


    def check_board(self):
        flag = False
        for i in range(5):
            pass
            #this is what i was working on last


def main():
    board = Board([[67, 97, 50, 51, 1],[47, 15, 77, 31, 66], [24, 14, 55, 70, 52], [76, 46, 19, 32, 73], [34, 22, 54, 75, 17]])    
    print(board.rows(0))
    print(board.diags())


if __name__ == "__main__":
    main()