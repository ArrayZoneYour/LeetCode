# /usr/bin/python
# coding: utf-8


class Solution:
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if x == 0:
            return 0
        if n == 0:
            return 1
        factor = [0, 1]
        results = [1, x]
        pointer_r = 1
        while factor[pointer_r] * 2 <= abs(n):
            factor.append(factor[-1] * 2)
            results.append(results[-1] * results[-1])
            pointer_r += 1
        pointer_r -= 1
        while factor[-1] < abs(n):
            if factor[pointer_r] + factor[-1] <= abs(n):
                factor[-1] += factor[pointer_r]
                results[-1] *= results[pointer_r]
            pointer_r -= 1
        return results[-1] if n >= 0 else 1 / results[-1]


print(Solution().myPow(2.00000, 10))
print(Solution().myPow(2.10000, 3))
print(Solution().myPow(2.00000, -2))
