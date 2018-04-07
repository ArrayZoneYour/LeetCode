# /usr/bin/python
# coding: utf-8

import math


class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        sub = [nums[0]]
        for num in nums[1:]:
            if num > sub[-1]:
                sub.append(num)
            elif num < sub[0]:
                sub[0] = num
            else:
                pointer_r = len(sub) - 1
                pointer_l = 0
                while True:
                    pointer_index = (pointer_l + pointer_r + 1) // 2
                    if (pointer_index == 0 and num <= sub[pointer_index]) or \
                            sub[pointer_index-1] < num <= sub[pointer_index]:
                        sub[pointer_index] = num
                        break
                    elif num > sub[pointer_index]:
                        pointer_l = pointer_index
                    elif num < sub[pointer_index]:
                        pointer_r = pointer_index - 1
        return len(sub)


print(Solution().lengthOfLIS([4, 10, 4, 3, 8, 9]))
