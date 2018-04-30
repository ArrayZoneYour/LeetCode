# /usr/bin/python
# coding: utf-8


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        result = minimum = maximum = nums[0]
        for num in nums[1:]:
            maximum, minimum = max(num, num * maximum, num * minimum), min(num, num * maximum, num * minimum)
            result = max(result, maximum)
        return result


print(Solution().maxProduct([2,3,-2,4]))
print(Solution().maxProduct([-2,0,-1]))
print(Solution().maxProduct([-2, 3, -4]))
print(Solution().maxProduct([-4,-3,-2]))
