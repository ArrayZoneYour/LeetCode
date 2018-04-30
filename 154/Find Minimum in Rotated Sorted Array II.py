# /usr/bin/python
# coding: utf-8
import math


class Solution:
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        left_minimum = nums[0]
        length = len(nums)
        while nums[-1] == left_minimum and length > 1:
            nums.pop()
            length -= 1
        if length <= 2:
            return min(nums)
        if left_minimum < nums[-1]:
            return left_minimum
        left, right = 0, length - 1
        while right > left + 1:
            medium = math.floor((left + right) / 2)
            if nums[medium] >= left_minimum:
                left = medium + 1
            else:
                right = medium
        return min(nums[left], nums[right])


print(Solution().findMin([1,3,5]))
print(Solution().findMin([2,2,2,0,1]))
print(Solution().findMin([2, 2, 2, 0, 2]))
print(Solution().findMin([2, 0, 2, 2, 2]))
