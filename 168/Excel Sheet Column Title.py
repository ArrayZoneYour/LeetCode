# /usr/bin/python
# coding: utf-8


class Solution:
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        string = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""
        while n:
            if n % 26 == 0:
                if n == 26:
                    result += 'Z'
                    return result[::-1]
                else:
                    result += 'Z'
                    n -= 26
            else:
                result += string[n % 26]
            n //= 26
        return result[::-1]


print(Solution().convertToTitle(1))
print(Solution().convertToTitle(28))
print(Solution().convertToTitle(701))
print(Solution().convertToTitle(52))
