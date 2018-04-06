# /usr/bin/python
# coding: utf-8


class Solution:
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_sum = sum(nums)
        if num_sum % 2:
            return False
        bag = [False] * (num_sum//2 + 1)
        bag[0] = True
        for num in nums:
            for i in range(1, len(bag) + 1 - num):
                if bag[-i-num]:
                    if i == 1:
                        return True
                    bag[-i] = True
        return False


print(Solution().canPartition([1, 2, 3, 5]))
