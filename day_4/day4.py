import os, sys, time, math, copy

class Square:
    def __init__(self, value):
        self.value = int(value)
        self.marked = False

    def __str__(self):
        return str(self.value)

    def mark(self):
        self.marked = True

class Board:
    def __init__(self, grid):
        self._00 = Square(grid[0][0])
        self._01 = Square(grid[0][1])
        self._02 = Square(grid[0][2])
        self._03 = Square(grid[0][3])
        self._04 = Square(grid[0][4])
        self._10 = Square(grid[1][0])
        self._11 = Square(grid[1][1])
        self._12 = Square(grid[1][2])
        self._13 = Square(grid[1][3])
        self._14 = Square(grid[1][4])
        self._20 = Square(grid[2][0])
        self._21 = Square(grid[2][1])
        self._22 = Square(grid[2][2])
        self._23 = Square(grid[2][3])
        self._24 = Square(grid[2][4])
        self._30 = Square(grid[3][0])
        self._31 = Square(grid[3][1])
        self._32 = Square(grid[3][2])
        self._33 = Square(grid[3][3])
        self._34 = Square(grid[3][4])
        self._40 = Square(grid[4][0])
        self._41 = Square(grid[4][1])
        self._42 = Square(grid[4][2])
        self._43 = Square(grid[4][3])
        self._44 = Square(grid[4][4])

    def __str__(self):
        ls = list()
        out = ""
        for i in range(5):
            ls.append(self.rows(i))
        for item in ls:
            for part in item:
                out += f"{part} "
            out += "\n"
        return out

    def rows(self, row):
        rs = list()
        for i in range(5):
            rs.append(eval(f"self._{row}{i}"))
        return rs

    def cols(self, col):
        rs = list()
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


    def mark(self, val):
        for i in range(5):
            for j in range(5):
                if eval(f"self._{i}{j}.marked") == False:
                    if eval(f"self._{i}{j}.value") == val:
                        eval(f"self._{i}{j}.mark()")


    def check_rows(self, marked):
        flag = False
        for i in range(5):
            for item in self.rows(i):
                if item in marked:
                    flag = True
                    continue
                else:
                    flag = False
                    break
        if flag == True:
            return True
        return False


    def check_cols(self, marked):
        flag = False
        for i in range(5):
            for item in self.cols(i):
                if item in marked:
                    flag = True
                    continue
                else:
                    flag = False
                    break
        if flag == True:
            return True
        return False


    def check_diags(self, marked):
        flag = False
        for item in self.diags():
            for part in item:
                if part in marked:
                    flag = True
                    continue
                else:
                    flag = False
                    break
        if flag == True:
            return True
        return False



    def check_board(self, ls):
        marked = list()
        for i in range(5):
            for j in range(5):
                if eval(f"self._{i}{j}.marked") == True:
                    marked.append(eval(f"self._{i}{j}"))
    
        if self.check_rows == True or self.check_cols == True or self.check_diags == True:
            return True
        else:
            return False
        


def main():
    boards = list()
    numbers = list()

    with open("input.txt", "r") as f:
        i = 0
        temp = list()
        for item in f:
            #print(item)
            if i == 0:
                i += 1
                numbers.append(item)
            else:
                if item == "\n" or item == "":
                    continue
                else:
                    temp.append(item.split())
                    if len(temp) == 5:
                        boards.append(Board(copy.deepcopy(temp)))
                        temp = list()
            
    print(numbers)
    for board in boards:
        print(board)
    lst = [34, 46, 34, 56, 55, 70, 91, 66, 1, 31, 42, 9]
    #print(board.check_board(lst))


if __name__ == "__main__":
    main()