# /usr/bin/python
# coding: utf-8


class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)):
            while 0 < nums[index] <= len(nums) and nums[index] != index + 1:
                if nums[nums[index]-1] == nums[index]:
                    break
                nums[nums[index]-1], nums[index] = nums[index], nums[nums[index]-1]
        for index in range(len(nums)):
            if nums[index] != index+1:
                return index + 1
        return len(nums) + 1


print(Solution().firstMissingPositive([1,2,0]))
print(Solution().firstMissingPositive([3,4,-1,1]))
print(Solution().firstMissingPositive([7,8,9,11,12]))
print(Solution().firstMissingPositive([3,4,1,2]))
print(Solution().firstMissingPositive([1,1,2]))
print(Solution().firstMissingPositive([1,1]))
