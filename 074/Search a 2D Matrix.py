# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        row_start = 0
        row_end = len(matrix) - 1
        if target >= matrix[row_end][0]:
            target_row = row_end
        elif target < matrix[row_start][0]:
            return False
        else:
            while row_start < row_end - 1:
                row_middle = math.floor((row_start + row_end) / 2)
                if matrix[row_middle][0] <= target:
                    row_start = row_middle
                else:
                    row_end = row_middle
            target_row = row_start
        if target > matrix[target_row][-1]:
            return False
        elif target == matrix[target_row][-1]:
            return True
        else:
            col_start = 0
            col_end = len(matrix[target_row]) - 1
            while col_start < col_end - 1:
                col_middle = math.floor((col_start + col_end) / 2)
                if matrix[target_row][col_middle] <= target:
                    col_start = col_middle
                else:
                    col_end = col_middle
            return col_start == col_end - 1 and matrix[target_row][col_start] == target


print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3))
print(Solution().searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13))
print(Solution().searchMatrix([
    [4]
], 4))
print(Solution().searchMatrix([
    [4]
], 3))
print(Solution().searchMatrix([
    [4],
    [5]
], 5))
