# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result = [-1, -1]
        pointer_l = 0
        pointer_r = len(nums) - 1
        if pointer_l == pointer_r:
            return [0, 0] if target == nums[0] else result
        while pointer_l <= pointer_r:
            pointer_m = math.floor((pointer_l + pointer_r) / 2)
            if nums[pointer_l] == target:
                result[0] = pointer_l
                break
            if pointer_l + 1 == pointer_r:
                result[0] = pointer_r if nums[pointer_r] == target and nums[pointer_l] != target else -1
                break
            if pointer_l == pointer_r:
                result[0] = pointer_l if nums[pointer_l] == target else -1
                break
            if nums[pointer_m] >= target:
                pointer_r = pointer_m
            else:
                pointer_l = pointer_m + 1
        if result[0] == -1:
            return result
        pointer_l = result[0]
        pointer_r = len(nums) - 1
        while pointer_l <= pointer_r:
            pointer_m = math.floor((pointer_l + pointer_r) / 2)
            if nums[pointer_r] == target:
                result[1] = pointer_r
                break
            if pointer_l + 1 == pointer_r:
                result[1] = pointer_l if nums[pointer_l] == target and nums[pointer_r] != target else -1
                break
            if pointer_l == pointer_r:
                result[0] = pointer_l if nums[pointer_l] == target else -1
                break
            if nums[pointer_m] > target:
                pointer_r = pointer_m - 1
            else:
                pointer_l = pointer_m
        return result


print(Solution().searchRange([5,7,7,8,8,10], 8))
print(Solution().searchRange([5,7,7,8,8,10], 6))
print(Solution().searchRange([5,5,7,7,8,8,10], 5))
print(Solution().searchRange([5,7,7,8,8,10], 5))
print(Solution().searchRange([5,7,7,8,8,10], 7))
print(Solution().searchRange([5,7,7,8,8,10], 10))
print(Solution().searchRange([5], 5))
print(Solution().searchRange([5,6], 5))
print(Solution().searchRange([4,5], 5))
print(Solution().searchRange([-3,-2,-1], 0))
