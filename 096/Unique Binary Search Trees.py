# /usr/bin/python
# coding: utf-8


class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = [1, 1]
        for i in range(2, n+1):
            num = 0
            for j in range(i):
                num += nums[j] * nums[i-1-j]
            nums.append(num)
        return nums[n]


print(Solution().numTrees(3))
