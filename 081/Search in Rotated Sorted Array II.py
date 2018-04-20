# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """
        if not nums:
            return False
        if len(nums) == 1:
            return nums[0] == target
        if nums[0] == target:
            return True
        flipped = False
        if nums[0] >= nums[-1]:
            flipped = True
        left = 0
        right = len(nums) - 1
        if flipped:
            while left < right:
                middle = math.floor((left + right) / 2)
                if nums[middle] < nums[0]:
                    right = middle
                else:
                    if nums[middle] == nums[0] and middle != 0:
                        del nums[middle]
                        right -= 1
                        continue
                    else:
                        left = middle + 1
            if target > nums[0]:
                left = 0
            elif target < nums[0]:
                right = len(nums) - 1
            else:
                return True
        while left < right:
            middle = math.floor((left + right) / 2)
            if target < nums[middle]:
                right = middle
            elif target > nums[middle]:
                left = middle + 1
            else:
                return True
        return left == right and nums[left] == target


print(Solution().search([2, 2, 0, 1], 1))  # True
print(Solution().search([2, 2, 2, 0, 2, 2], 0))  # True
print(Solution().search([1, 3, 1, 1, 1], 3))  # True
print(Solution().search([2, 2, 0], 0))  # True
print(Solution().search([2, 1], 1))  # True
print(Solution().search([3,3,6,6,1,1,2,2], 2))  # True
print(Solution().search([0,1,2,5,6,0], 6))  # True
print(Solution().search([2,5,6,0,0,1,2], 0))  # True
print(Solution().search([3,1,1], 3))  # True
print(Solution().search([3,3,1,1], 3))  # True
print(Solution().search([3,3,6,6,1,1], 6))  # True
print(Solution().search([2, 2, 0], 2))  # True
print(Solution().search([2, 2, 0, 1], 0))  # True
print(Solution().search([0], 0))  # True
print(Solution().search([1, 1], 1))  # True
print(Solution().search([1, 2], 1))  # True
print(Solution().search([0], 3))  # False
print(Solution().search([2, 2], 1))  # False
print(Solution().search([3, 2], 1))  # False
print(Solution().search([1, 1, 3], 2))  # False
print(Solution().search([0, 2, 2], 3))  # False
print(Solution().search([2,5,6,0,0,1,2], 3))  # False

