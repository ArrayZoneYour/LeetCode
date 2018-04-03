# /usr/bin/python
# coding: utf-8


class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        length = len(triangle)
        if length == 1:
            return triangle[0][0]
        for level in range(1, len(triangle)):
            triangle[level][0] = triangle[level-1][0] + triangle[level][0]
            triangle[level][-1] = triangle[level-1][-1] + triangle[level][-1]
            for index in range(1, level):
                triangle[level][index] = min(triangle[level-1][index-1], triangle[level-1][index]) + triangle[level][index]
        return min(triangle[-1])

