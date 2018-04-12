# /usr/bin/python
# coding: utf-8


class Solution:
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        if len(nums) > 1:
            swap_index_left = -2
            while abs(swap_index_left) <= len(nums) and nums[swap_index_left] >= nums[swap_index_left+1]:
                swap_index_left -= 1
            if abs(swap_index_left) == len(nums) + 1:
                nums.reverse()
            else:
                swap_index_right = -1
                while swap_index_left < swap_index_right and nums[swap_index_right] <= nums[swap_index_left]:
                    swap_index_right -= 1
                nums[swap_index_left], nums[swap_index_right] = nums[swap_index_right], nums[swap_index_left]
                l = swap_index_left + 1
                r = -1
                while l < r:
                    nums[l], nums[r] = nums[r], nums[l]
                    l, r = l + 1, r - 1
                return nums


print(Solution().nextPermutation([5, 1, 1]))
