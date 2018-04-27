# /usr/bin/python
# coding: utf-8


class Solution:

    def singleNumber(self, nums):
        ones = 0
        twos = 0
        for num in nums:
            ones = (ones ^ num) & ~twos
            twos = (twos ^ num) & ~ones
        return ones

    # Solution hash_table
    # def singleNumber(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     memo = {}
    #     while nums:
    #         num = nums.pop()
    #         if num not in memo:
    #             memo[num] = 1
    #         else:
    #             if memo[num] == 2:
    #                 memo.pop(num)
    #             else:
    #                 memo[num] += 1
    #     return list(memo.keys())[0]


print(Solution().singleNumber([2,2,3,2]))
print(Solution().singleNumber([0,1,0,1,0,1,99]))
