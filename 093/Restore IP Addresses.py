# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.valid_results = []

    def makeValidAddress(self, s, result, length):
        if length == 4 and not s:
            self.valid_results.append(".".join(result))
        s_length = len(s) if len(s) < 3 else 3
        for i in range(s_length):
            if i == 0 or (s[0] != '0' and int(s[:i+1]) < 256):
                result.append(s[:i+1])
                self.makeValidAddress(s[i+1:], result, length + 1)
                result.pop()

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) < 4 or len(s) > 16:
            return []
        for i in range(3):
            if i == 0:
                self.makeValidAddress(s[1:], [s[0]], 1)
            if i == 1 and s[0] != '0':
                self.makeValidAddress(s[2:], [s[:2]], 1)
            if i == 2 and s[0] != '0' and int(s[:3]) < 256:
                self.makeValidAddress(s[3:], [s[:3]], 1)
        return self.valid_results


print(Solution().restoreIpAddresses("010010"))
