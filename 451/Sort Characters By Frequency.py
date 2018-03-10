# /usr/bin/python
# coding: utf-8

from collections import Counter


class Solution:
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = ""
        for el in Counter(s).most_common():
            result += el[0] * el[1]
        return result


if __name__ == '__main__':
    assert Solution().frequencySort("tree") == "eetr"
    assert Solution().frequencySort("cccaaa") == "cccaaa"
    assert Solution().frequencySort("Aabb") == "bbAa"