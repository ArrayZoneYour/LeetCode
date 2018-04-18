# /usr/bin/python
# coding: utf-8


class Solution:
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        farthest_index = 0
        nearest_index = 0
        while farthest_index < len(nums) - 1:
            last_farthest_index = farthest_index
            for index in range(nearest_index, farthest_index + 1):
                if nums[index] + index > farthest_index:
                    farthest_index = nums[index] + index
            if farthest_index > last_farthest_index:
                nearest_index = last_farthest_index + 1
            else:
                return False
        return True


print(Solution().canJump([1,1,1,0]))
print(Solution().canJump([1,1,0,1]))
print(Solution().canJump([2,5,0,0]))
print(Solution().canJump([2,3,1,1,4]))
print(Solution().canJump([3,2,1,0,4]))
