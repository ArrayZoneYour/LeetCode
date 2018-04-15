# /usr/bin/python
# coding: utf-8


class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row_status = [[False for i in range(10)] for j in range(9)]
        col_status = [[False for i in range(10)] for j in range(9)]
        box_status = [[False for i in range(10)] for j in range(9)]
        for row in range(9):
            for col in range(9):
                if board[row][col] != '.':
                    num = int(board[row][col])
                    box_num = row//3*3+col//3
                    if row_status[row][num] or col_status[col][num] or box_status[box_num][num]:
                        return False
                    row_status[row][num] = col_status[col][num] = box_status[box_num][num] = True
        return True


print(Solution().isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
print(Solution().isValidSudoku([
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]))
