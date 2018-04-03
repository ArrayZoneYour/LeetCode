# /usr/bin/python
# coding: utf-8


class Solution:
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        steps = [1, 1, 2]
        if n > 2:
            for i in range(3, n+1):
                steps.append(steps[i-1] + steps[i-2])
        return steps[n]


print(Solution().climbStairs(3))
