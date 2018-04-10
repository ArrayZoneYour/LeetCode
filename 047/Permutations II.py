# /usr/bin/python
# coding: utf-8
from collections import Counter


class Solution:
    def _permuteUnique(self, counter, result, results, max_length):
        if len(result) == max_length:
            results.append(result.copy())
        else:
            for num in counter:
                if counter[num]:
                    counter[num] -= 1
                    result.append(num)
                    self._permuteUnique(counter, result, results, max_length)
                    result.pop()
                    counter[num] += 1

    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        max_length = len(nums)
        results = []
        nums_counter = Counter(nums)
        for num in nums_counter:
            nums_counter[num] -= 1
            self._permuteUnique(nums_counter, [num], results, max_length)
            nums_counter[num] += 1
        return results

