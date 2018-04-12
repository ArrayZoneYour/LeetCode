# /usr/bin/python
# coding: utf-8


class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(needle) > len(haystack):
            return -1
        decide_times = len(haystack) - len(needle) + 1
        for i in range(decide_times):
            if needle == haystack[i:i+len(needle)]:
                return i
        return -1


print(Solution().strStr("hello", "ll"))
print(Solution().strStr("aaaaa", "aba"))
