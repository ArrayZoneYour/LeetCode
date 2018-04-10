# /usr/bin/python
# coding: utf-8


class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        length = len(nums)
        result = sum(nums[:3])
        for i in range(length - 2):
            pointer_l = i + 1
            pointer_r = length - 1
            while pointer_l < pointer_r:
                cur_sum = nums[pointer_l] + nums[pointer_r] + nums[i]
                if abs(cur_sum - target) < abs(result - target):
                    result = cur_sum
                if cur_sum < target:
                    pointer_l += 1
                elif cur_sum > target:
                    pointer_r -= 1
                else:
                    return target
        return result


if __name__ == '__main__':
    assert Solution().threeSumClosest([-1, 2, 1, -4], 1) == 2
    # assert Solution().threeSumClosest([1,2,4,8,16,32,64,128], 82) ==
