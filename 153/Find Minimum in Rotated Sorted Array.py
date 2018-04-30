# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return min(nums)
        left = 0
        right = len(nums) - 1
        left_minimum = nums[0]
        if left_minimum > nums[-1]:
            while right > left + 1:
                medium = math.floor((left + right) / 2)
                if nums[medium] > left_minimum:
                    left = medium + 1
                else:
                    right = medium
            return min(nums[left], nums[right])
        else:
            return left_minimum


print(Solution().findMin([3,4,5,1,2]))
print(Solution().findMin([0,1,2,4,5,6,7]))
print(Solution().findMin([4,5,6,7,0,1,2]))
