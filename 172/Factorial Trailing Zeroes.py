# /usr/bin/python
# coding: utf-8


class Solution:
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        while n >= 5:
            n //= 5
            result += n
        return result


print(Solution().trailingZeroes(3))
print(Solution().trailingZeroes(5))
print(Solution().trailingZeroes(25))
