# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if not nums:
            return -1
        if len(nums) == 1:
            return 0 if nums[0] == target else -1
        if len(nums) == 2:
            if nums[0] == target:
                return 0
            if nums[1] == target:
                return 1
            return -1
        # binary search minmum
        pointer_l = 0
        pointer_r = len(nums) - 1
        if nums[pointer_l+1] < nums[pointer_l] < nums[-1] \
                or nums[pointer_l + 1] > nums[pointer_l] > nums[-1]\
                or nums[pointer_r-1] < nums[pointer_r] < nums[pointer_l]\
                or nums[pointer_r-1] > nums[pointer_r] > nums[pointer_l]:
            while pointer_l <= pointer_r:
                pointer_m = math.floor((pointer_l + pointer_r) / 2)
                if pointer_m == pointer_r and nums[pointer_m] < nums[0]:
                    break
                if nums[pointer_m] < nums[pointer_m + 1] and nums[pointer_m] < nums[pointer_m - 1]:
                    break
                elif nums[pointer_m] > nums[0]:
                    pointer_l = pointer_m + 1
                elif nums[pointer_m] < nums[0]:
                    pointer_r = pointer_m - 1
                if pointer_r == pointer_l + 1:
                    pointer_m = pointer_l if nums[pointer_l] < nums[pointer_r] else pointer_r
                    break
            if pointer_l > pointer_r:
                return -1
            if target < nums[pointer_m] or target > nums[pointer_m-1]:
                return -1
            if target >= nums[0]:
                pointer_l = 0
                pointer_r = pointer_m - 1
            else:
                pointer_l = pointer_m
                pointer_r = len(nums) - 1
        while pointer_l <= pointer_r:
            pointer_m = math.floor((pointer_l + pointer_r) / 2)
            if nums[pointer_m] > target:
                pointer_r = pointer_m - 1
            elif nums[pointer_m] < target:
                pointer_l = pointer_m + 1
            else:
                return pointer_m
        return -1


print(Solution().search([5, 6, 7, 2, 3, 4], 5))
print(Solution().search([4,5,6,7,0,1,2], 2))
print(Solution().search([4,5,6,7,0,1,2], 3))
print(Solution().search([1], 0))
print(Solution().search([1, 3], 1))
print(Solution().search([1, 3], 3))
print(Solution().search([1, 5], 3))
print(Solution().search([1, 3, 5], 0))
print(Solution().search([1, 3, 5], 3))
print(Solution().search([5, 1, 2, 3, 4], 4))
print(Solution().search([5, 1, 3], 5))
