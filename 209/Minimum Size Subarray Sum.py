# /usr/bin/python
# coding: utf-8


class Solution:
    def minSubArrayLen(self, s, nums):
        """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        # 初始化变量
        pointer_l = 0
        pointer_r = 0
        result = 0
        if not nums:
            return result
        else:
            _sum = nums[0]
        # 搜索是否有解
        while _sum < s and pointer_r != len(nums) - 1:
            pointer_r += 1
            _sum += nums[pointer_r]
        # 继续搜寻最优解
        while pointer_r != len(nums) and pointer_l != len(nums):
            if _sum >= s:
                result = pointer_r - pointer_l + 1
                _sum -= nums[pointer_l]
                pointer_l += 1
            else:
                _sum -= nums[pointer_l]
                pointer_l += 1
                pointer_r += 1
                if pointer_r == len(nums):
                    return result
                _sum += nums[pointer_r]
        return result


if __name__ == '__main__':
    assert Solution().minSubArrayLen(4, [1, 4, 4]) == 2
