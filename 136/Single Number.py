# /usr/bin/python
# coding: utf-8


class Solution:

    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     memo = {}
    #     while nums:
    #         num = nums.pop()
    #         if num not in memo:
    #             memo[num] = True
    #         else:
    #             memo.pop(num)
    #     return list(memo.keys())[0]

    def singleNumber(self, nums):
        ones = 0
        for num in nums:
            ones ^= num
        return ones


print(Solution().singleNumber([2,2,1]))
print(Solution().singleNumber([4,1,2,1,2]))
