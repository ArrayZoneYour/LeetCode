# /usr/bin/python
# coding: utf-8


class Solution:

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # nums.sort()
        counts = [0] * (target+1)
        counts[0] = 1
        for index in range(target+1):
            for num in nums:
                if index - num >= 0:
                    counts[index] += counts[index - num]
        return counts[-1]


print(Solution().combinationSum4([4, 2, 1], 32))
