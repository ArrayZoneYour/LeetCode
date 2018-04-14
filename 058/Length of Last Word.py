# /usr/bin/python
# coding: utf-8


class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        s = s.rstrip(' ')
        return len(s.split(' ')[-1])


print(Solution().lengthOfLastWord('a    '))
