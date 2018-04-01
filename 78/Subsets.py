# /usr/bin/python
# coding: utf-8


class Solution:
    def subset(self, nums, result, results):
        if nums:
            self.subset(nums[1:], result, results)
            result.append(nums[0])
            self.subset(nums[1:], result, results)
            result.pop()
        else:
            results.append(result.copy())

    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        if nums:
            self.subset(nums[1:], [], results)
            self.subset(nums[1:], [nums[0]], results)
        return results
