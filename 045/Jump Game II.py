# /usr/bin/python
# coding: utf-8


class Solution:
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        jump_times = 0
        max_dis = 0
        index = 0
        while max_dis < len(nums) - 1:
            stop_index = max_dis
            while index <= stop_index:
                if index + nums[index] > max_dis:
                    max_dis = index + nums[index]
                index += 1
            jump_times += 1
        return jump_times


print(Solution().jump([2,3,1,1,4]))
