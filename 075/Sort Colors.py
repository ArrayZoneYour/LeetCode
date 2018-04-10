# /usr/bin/python
# coding: utf-8


class Solution:
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        point_l = 0  # 0 元素的左边界
        point_r = 0  # 0 元素的右边界
        two_l = len(nums)  # 2 元素的左边界
        while point_r < two_l:
            if nums[point_r] == 0:
                nums[point_l], nums[point_r] = nums[point_r], nums[point_l]
                point_r += 1
                point_l += 1
            elif nums[point_r] == 1:
                point_r += 1
            else:
                nums[point_r], nums[two_l - 1] = nums[two_l - 1], nums[point_r]
                two_l -= 1


if __name__ == '__main__':
    nums = [0, 2, 1, 2, 0, 1]
    Solution().sortColors(nums)
    assert nums == [0, 0, 1, 1, 2, 2]
    nums = [0, 2]
    Solution().sortColors(nums)
    assert nums == [0, 2]
