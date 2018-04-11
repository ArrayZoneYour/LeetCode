# /usr/bin/python
# coding: utf-8


class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not strs:
            return ''
        max_str = ''
        min_str = strs[0]
        for _str in strs:
            if _str > max_str:
                max_str = _str
            elif _str < min_str:
                min_str = _str
        max_length = min(len(max_str), len(min_str))
        for i in range(max_length):
            if max_str[i] != min_str[i]:
                return max_str[:i]
        return min_str


print(Solution().longestCommonPrefix(['daa', 'da', 'dafr']))
