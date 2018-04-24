# /usr/bin/python
# coding: utf-8


class Solution:
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """
        m, n = len(s), len(t)
        dp = [[0 for row in range(m+1)] for col in range(n+1)]
        dp[0] = [1 for row in range(m+1)]
        for row in range(1, n+1):
            for col in range(1, m+1):
                dp[row][col] = dp[row][col-1]
                if s[col-1] == t[row-1]:
                    dp[row][col] += dp[row-1][col-1]
        return dp[-1][-1]
