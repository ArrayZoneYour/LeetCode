# /usr/bin/python
# coding: utf-8


class Solution:
    def rob_subset(self, nums):
        pre_pre = nums[0]
        pre = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            cur = max(pre, pre_pre + nums[i])
            pre_pre = pre
            pre = cur
        return pre

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        return max(self.rob_subset(nums[1:]), self.rob_subset(nums[:-1]))


print(Solution().rob([1, 2, 1, 0]))
