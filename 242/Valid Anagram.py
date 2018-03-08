# /usr/bin/python
# coding: utf-8

from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = Counter(s)
        t = Counter(t)
        return s == t


if __name__ == '__main__':
    assert Solution().isAnagram("anagram", "nagaram") is True
