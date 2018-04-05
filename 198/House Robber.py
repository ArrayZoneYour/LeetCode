# /usr/bin/python
# coding: utf-8


class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        house_num = len(nums)
        if house_num <= 2:
            return max(nums)
        else:
            rob_maximum = [0 for i in range(house_num)]
            rob_maximum[0], rob_maximum[1] = nums[0], max(nums[0], nums[1])
            for i in range(2, house_num):
                rob_maximum[i] = max(rob_maximum[i-1], rob_maximum[i-2] + nums[i])
            return rob_maximum[-1]

