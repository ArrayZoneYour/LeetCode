# /usr/bin/python
# coding: utf-8


class Solution:
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        length = len(s)
        result = set()
        stop_index = length - 9
        sequence_table = set()
        for index in range(stop_index):
            sequence = s[index:index+10]
            if sequence not in sequence_table:
                sequence_table.add(sequence)
            else:
                result.add(sequence)
        return [sequence for sequence in result]


print(Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"))
