# /usr/bin/python
# coding: utf-8


class Solution:
    def findKthLargest(self, nums, k):
        """
        利用快排partition操作中pivot会被放在正确位置的性质
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums = sorted(nums)
        nums.reverse()
        return nums[k-1]


if __name__ == '__main__':
    assert Solution().findKthLargest([3, 1, 2, 4], 2) == 3
    assert Solution().findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert Solution().findKthLargest([-1, -1], 2) == -1
    assert Solution().findKthLargest([99, 99], 1) == 99
