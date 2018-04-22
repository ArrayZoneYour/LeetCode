# /usr/bin/python
# coding: utf-8


class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        m, n, p = len(s1), len(s2), len(s3)
        if m + n != p:
            return False
        dp = [[False for i in range(n+1)] for j in range(m+1)]
        dp[0][0] = True
        for row in range(m+1):
            for col in range(n+1):
                if row == 0:
                    dp[row][col] = s2[:col] == s3[:col]
                elif col == 0:
                    dp[row][col] = s1[:row] == s3[:row]
                else:
                    dp[row][col] = dp[row-1][col] and s1[row-1] == s3[row+col-1] or \
                                   dp[row][col-1] and s2[col-1] == s3[row+col-1]
        return dp[-1][-1]


print(Solution().isInterleave("aabcc", "dbbca", "aadbbbaccc"))
