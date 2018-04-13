# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return 0
        pointer_l = 0
        pointer_r = len(nums) - 1
        if target > nums[pointer_r]:
            return pointer_r + 1
        if target < nums[0]:
            return 0
        while pointer_r - pointer_l != 1:
            pointer_m = math.floor((pointer_r + pointer_l) / 2)
            if nums[pointer_m] > target:
                pointer_r = pointer_m
            elif nums[pointer_m] < target:
                pointer_l = pointer_m
            else:
                return pointer_m
        return pointer_l if target == nums[pointer_l] else pointer_r


print(Solution().searchInsert([1,3,5,6], 5))
print(Solution().searchInsert([1,3,5,6], 2))
print(Solution().searchInsert([1,3,5,6], 7))
print(Solution().searchInsert([1,3,5,6], 0))
