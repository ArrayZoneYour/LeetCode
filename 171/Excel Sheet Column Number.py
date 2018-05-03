# /usr/bin/python
# coding: utf-8


class Solution:
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = 0
        for el in s:
            result *= 26
            result += ord(el) - 64
        return result


print(Solution().titleToNumber("A"))
print(Solution().titleToNumber("AB"))
print(Solution().titleToNumber("ZY"))
