# /usr/bin/python
# coding: utf-8

import math


class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return n
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1
        cnt = 0
        arrive_points = {n}
        while arrive_points:
            cnt += 1
            temp = set()
            for x in arrive_points:
                for y in squares:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            arrive_points = temp
        return cnt



print(Solution().numSquares(7168))
assert Solution().numSquares(12) == 3
