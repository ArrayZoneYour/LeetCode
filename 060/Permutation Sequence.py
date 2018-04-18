# /usr/bin/python
# coding: utf-8


class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        nums = [n+1 for n in range(n)]
        factor = [1]
        for i in range(2, n):
            factor.append(factor[-1]*i)
        result = ''
        while len(factor) > 0:
            pop_index = (k-1) // factor[-1]
            result += str(nums[pop_index])
            k %= factor[-1]
            del nums[pop_index]
            del factor[-1]
        if nums:
            result += str(nums[0])
        return result


print(Solution().getPermutation(1, 1))
print(Solution().getPermutation(4, 9))
print(Solution().getPermutation(3, 6))
print(Solution().getPermutation(3, 3))
