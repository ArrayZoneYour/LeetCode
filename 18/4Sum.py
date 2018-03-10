# /usr/bin/python
# coding: utf-8


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


if __name__ == '__main__':
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-1, 0, 0, 1],
        [-2, -1, 1, 2],
        [-2, 0, 0, 2]
    ]
