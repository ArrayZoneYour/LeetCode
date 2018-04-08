# /usr/bin/python
# coding: utf-8


class Solution:
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_len = len(s)
        s_index = 0
        if not s:
            return True
        for t_el in t:
            if s[s_index] == t_el:
                s_index += 1
            if s_index == s_len:
                break
        return s_index == s_len


assert Solution().isSubsequence("abc", "ahbgdc") is True
assert Solution().isSubsequence("axc", "ahbgdcx") is False
