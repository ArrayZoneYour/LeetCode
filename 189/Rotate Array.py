# /usr/bin/python
# coding: utf-8


class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        rotate_times = k % len(nums)
        # for i in range(rotate_times):
        #     el = nums.pop()
        #     nums.insert(0, el)
        if rotate_times != 0:
            nums[:rotate_times], nums[rotate_times:] = nums[-rotate_times:], nums[:-rotate_times]
        return nums


print(Solution().rotate([-1], 2))
print(Solution().rotate([1,2,3,4,5,6,7], 3))
print(Solution().rotate([-1,-100,3,99], 2))
print(Solution().rotate([1], 1))
print(Solution().rotate([1, 2], 3))
