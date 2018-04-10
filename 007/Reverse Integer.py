# /usr/bin/python
# coding: utf-8


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        x = str(x)
        if x == '0' or x == '-0':
            return int(x)
        x = x.rstrip('0')
        if x.startswith('-'):
            if len(x) > 11:
                return 0
            overflow = '2147483648'
            if len(x) == 11:
                for index, s in enumerate(x[-1:0:-1]):
                    if ord(s) < ord(overflow[index]):
                        break
                    if ord(s) > ord(overflow[index]):
                        return 0
            return int('-' + x[-1:0:-1])
        else:
            if len(x) > 10:
                return 0
            overflow = '2147483647'
            if len(x) == 10:
                for index, s in enumerate(x[::-1]):
                    if ord(s) < ord(overflow[index]):
                        break
                    if ord(s) > ord(overflow[index]):
                        return 0
            return int(x[::-1])


print(Solution().reverse(123))
print(Solution().reverse(-123))
print(Solution().reverse(120))
print(Solution().reverse(7463847412))
print(Solution().reverse(-1474836481))
