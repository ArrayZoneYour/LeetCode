# /usr/bin/python
# coding: utf-8


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """


if __name__ == '__main__':
    assert Solution().wordPattern("abba", "dog cat cat dog") is True
    assert Solution().wordPattern("abba", "dog cat cat fish") is False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
    assert Solution().wordPattern("abba", "dog dog dog dog") is False
