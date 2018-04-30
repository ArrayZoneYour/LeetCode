# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        while right > left + 1:
            mid = math.floor((left + right) / 2)
            mid_left = nums[mid - 1]
            mid_right = nums[mid + 1]
            mid_num = nums[mid]
            if mid_num > mid_left and mid_num > mid_right:
                return mid
            elif mid_num > mid_left:
                left = mid
            else:
                right = mid
        return left if nums[left] > nums[right] else right


print(Solution().findPeakElement([1, 2, 3, 1]))
print(Solution().findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(Solution().findPeakElement([1]))
print(Solution().findPeakElement([1, 2]))
print(Solution().findPeakElement([2, 1]))
print(Solution().findPeakElement([1, 2, 3]))
print(Solution().findPeakElement([3, 2, 1]))
print(Solution().findPeakElement([2, 1, 3]))
