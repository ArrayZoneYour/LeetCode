# /usr/bin/python
# coding: utf-8


class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maximum = nums[0]
        cur_sum = 0
        for i in range(len(nums)):
            cur_sum += nums[i]
            if cur_sum > maximum:
                maximum = cur_sum
            if cur_sum < 0:
                cur_sum = 0
        return maximum


print(Solution().maxSubArray([1]))
