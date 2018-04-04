# /usr/bin/python
# coding: utf-8


class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        results = [[0 for i in range(n)] for j in range(m)]
        for row in range(m):
            results[row][0] = 1
        for col in range(n):
            results[0][col] = 1
        if m > 1 and n > 1:
            for row in range(1, m):
                for col in range(1, n):
                    results[row][col] = results[row-1][col] + results[row][col-1]
        return results[-1][-1]

