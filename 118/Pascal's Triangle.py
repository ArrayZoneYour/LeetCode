# /usr/bin/python
# coding: utf-8


class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        for i in range(numRows):
            row = [1]
            for index in range(1, i):
                row.append(result[i-1][index-1] + result[i-1][index])
            if i > 0:
                row.append(1)
            result.append(row.copy())
        return result


print(Solution().generate(5))
