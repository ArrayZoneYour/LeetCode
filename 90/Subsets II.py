# /usr/bin/python
# coding: utf-8


class Solution:
    def subsetAllowDup(self, nums, old_value, result, results):
        if nums:
            flag = True
            for idx, num in enumerate(nums):
                if num != old_value:
                    flag = False
                    result.append(num)
                    self.subsetAllowDup(nums[idx+1:], old_value, result, results)
                    result.pop()
                    old_value = num
                    self.subsetAllowDup(nums[idx+1:], old_value, result, results)
                    break
            if flag:
                self.subsetAllowDup([], old_value, result, results)
        else:
            results.append(result.copy())

    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # You can use the hash table to count the num of el and revert the hash table to list and
        # complete the question to advance the performance
        results = []
        nums.sort()
        old_value = None
        if nums:
            for idx, num in enumerate(nums):
                if num != old_value:
                    self.subsetAllowDup(nums[idx+1:], old_value, [num], results)
                    old_value = num
                    self.subsetAllowDup(nums[idx+1:], old_value, [], results)
                    break
        return results

