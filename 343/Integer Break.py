# /usr/bin/python
# coding: utf-8


class Solution:
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        max_break = [0, 0, 1, 2, 4, 6, 9]
        if n < 6:
            return max_break[n]
        else:
            for i in range(6, n+1):
                max_break.append(max(2*max_break[-2], 3*max_break[-3], 4*max_break[-4], (i//2)*(i-i//2)))
        return max_break[n]

