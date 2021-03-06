# /usr/bin/python
# coding: utf-8


class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        first_row_zero = False
        first_col_zero = False
        for el in matrix[0]:
            if el == 0:
                first_row_zero = True
                break
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                first_col_zero = True

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    matrix[0][col], matrix[row][0] = 0, 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if matrix[0][col] == 0 or matrix[row][0] == 0:
                    matrix[row][col] = 0

        if first_row_zero:
            for col in range(len(matrix[0])):
                matrix[0][col] = 0
        if first_col_zero:
            for row in range(len(matrix)):
                matrix[row][0] = 0
