# /usr/bin/python
# coding: utf-8


class Solution:
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        res = []
        i = 0
        while i < 1 << n:
            res.append(i ^ i >> 1)
            i += 1
        return res


print(Solution().grayCode(0))
print(Solution().grayCode(1))
print(Solution().grayCode(2))
