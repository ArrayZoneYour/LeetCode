# /usr/bin/python
# coding: utf-8
import copy


class Solution:
    def __init__(self):
        self.partitions = []

    def single_partition(self, s, result):
        if not s:
            self.partitions.append(result.copy())
        else:
            length = len(s)
            for i in range(length):
                if s[0:i+1] == s[i::-1]:
                    result.append(s[0:i+1])
                    self.single_partition(s[i+1:], result)
                    result.pop()

    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        length = len(s)
        for i in range(length):
            if s[0:i+1] == s[i::-1]:
                self.single_partition(s[i+1:], [s[0:i+1]])
        return self.partitions

