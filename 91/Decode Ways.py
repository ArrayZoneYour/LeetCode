# /usr/bin/python
# coding: utf-8


class Solution:
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or s[0] == '0':
            return 0
        length = len(s)
        if length == 1:
            return 1
        num = [0, 1, 2 if 10 < int(s[0:2]) <= 26 else 1]
        if int(s[0:2]) > 26 and s[1] == '0':
            return 0
        if s[0:2] == '20':
            num[2] = 1
        for i in range(3, length+1):
            if s[i-1:i] == '0':
                if s[i-2:i-1] == '1' or s[i-2:i-1] == '2':
                    num.append(num[-2])
                else:
                    return 0
            elif s[i-2:i-1] == '0':
                num.append(num[-1])
            else:
                num.append(num[-1] + num[-2] if int(s[i-2:i]) <= 26 else num[-1])
        return num[length]

