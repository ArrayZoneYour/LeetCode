# /usr/bin/python
# coding: utf-8


class Solution:
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip(' ')
        prefix = ''
        if not str:
            return 0
        if str[0] == '+' or str[0] == '-':
            if str[0] == '-':
                prefix = '-'
            str = str[1:]
        pointer_l = 0
        while pointer_l < len(str):
            if ord(str[pointer_l]) > ord('9') or ord(str[pointer_l]) < ord('0'):
                break
            pointer_l += 1
        str = str[:pointer_l]
        if str:
            if prefix == '-':
                if int(str) > 2147483648:
                    return -2147483648
            else:
                if int(str) > 2147483647:
                    return 2147483647
        return int(prefix + str) if str else 0


print(Solution().myAtoi('-+1'))
print(Solution().myAtoi('   789 '))
print(Solution().myAtoi('789&&&'))
print(Solution().myAtoi('$$789'))
print(Solution().myAtoi('+-1'))
print(Solution().myAtoi('-1'))
print(Solution().myAtoi("-2147483649"))
print(Solution().myAtoi("   -1123u3761867"))

