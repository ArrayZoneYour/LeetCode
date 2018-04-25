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
        buy_price = prices[0]
        for price in prices:
            if price > buy_price:
                profit += price - buy_price
                buy_price = price
            if price < buy_price:
                buy_price = price
        return profit


print(Solution().maxProfit([7,1,5,3,6,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))
