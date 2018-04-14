# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        return math.floor(math.sqrt(x))


print(Solution().mySqrt(8))
