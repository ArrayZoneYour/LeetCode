# /usr/bin/python
# coding: utf-8


class Solution:
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        pointer_l = 0
        pointer_r = len(numbers) - 1
        while pointer_r > pointer_l:
            if numbers[pointer_l] + numbers[pointer_r] > target:
                pointer_r -= 1
            elif numbers[pointer_r] + numbers[pointer_l] < target:
                pointer_l += 1
            else:
                return [pointer_l + 1, pointer_r + 1]


if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    assert Solution().twoSum(nums, 9) == [1, 2]
