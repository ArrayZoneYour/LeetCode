# /usr/bin/python
# coding: utf-8


class Solution:

    def __init__(self):
        self.row_status = []
        self.col_status = []
        self.box_status = []
        self.board = []
        self.done = False

    def scanBoard(self):
        for row in range(9):
            for col in range(9):
                if self.board[row][col] != '.':
                    num = int(self.board[row][col])
                    box_num = row // 3 * 3 + col // 3
                    # print(row, col, box_num, num)
                    self.row_status[row][num-1] = False
                    self.col_status[col][num-1] = False
                    self.box_status[box_num][num-1] = False

    def placeNum(self, row, col):
        if row == 9:
            self.done = True
            return
        next_row = row + 1 if col == 8 else row
        next_col = col + 1 if col != 8 else 0
        # print(row, col, next_row, next_col)
        if self.board[row][col] == '.':
            box_num = row // 3 * 3 + col // 3
            for num in range(9):
                if self.row_status[row][num] and self.col_status[col][num] and \
                   self.box_status[box_num][num]:
                    self.row_status[row][num] = False
                    self.col_status[col][num] = False
                    self.box_status[box_num][num] = False
                    self.board[row][col] = str(num+1)
                    self.placeNum(next_row, next_col)
                    if self.done:
                        return
                    self.board[row][col] = '.'
                    self.row_status[row][num] = True
                    self.col_status[col][num] = True
                    self.box_status[box_num][num] = True
        else:
            self.placeNum(next_row, next_col)

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.row_status = [[True for i in range(9)] for j in range(9)]
        self.col_status = [[True for i in range(9)] for j in range(9)]
        self.dia_status = [[True for i in range(9)] for j in range(2)]
        self.box_status = [[True for i in range(9)] for j in range(9)]
        self.scanBoard()
        self.placeNum(0, 0)


print(Solution().solveSudoku([[".",".","9","7","4","8",".",".","."],["7",".",".",".",".",".",".",".","."],[".","2",".","1",".","9",".",".","."],[".",".","7",".",".",".","2","4","."],[".","6","4",".","1",".","5","9","."],[".","9","8",".",".",".","3",".","."],[".",".",".","8",".","3",".","2","."],[".",".",".",".",".",".",".",".","6"],[".",".",".","2","7","5","9",".","."]]
))