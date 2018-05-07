# /usr/bin/python
# coding: utf-8


class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n > 0:
            result += n % 2
            n //= 2
        return result


print(Solution().hammingWeight(11))
print(Solution().hammingWeight(128))
