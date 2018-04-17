# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        center = (len(matrix) - 1) / 2
        for x in range(math.ceil(center), len(matrix)):
            for y in range(math.ceil(center), len(matrix)):
                dx, dy = x - center, y - center
                if dx > 0:
                    matrix[x][y], matrix[int(center + dy)][int(center - dx)], \
                    matrix[int(center - dx)][int(center - dy)], matrix[int(center - dy)][int(center + dx)] = \
                        matrix[int(center - dy)][int(center + dx)], matrix[x][y], \
                        matrix[int(center + dy)][int(center - dx)], matrix[int(center - dx)][int(center - dy)]
        return matrix


print(Solution().rotate([
  [1,2,3],
  [4,5,6],
  [7,8,9]
]))
print(Solution().rotate([
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]))
