# /usr/bin/python
# coding: utf-8


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        profit = 0
        min_cost = prices[0]
        for price in prices:
            if price - min_cost > profit:
                profit = price - min_cost
            if price < min_cost:
                min_cost = price
        return profit


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([7,6,4,3,1]))
