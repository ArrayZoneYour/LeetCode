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
        first_wait = [prices[0], -prices[0]]
        first_sell = 0
        second_wait = []
        profit = 0
        for price in prices[1:]:
            last_first_sell = first_sell
            first_wait[0] = price
            if sum(first_wait) > first_sell:
                first_sell = sum(first_wait)
            if sum(first_wait) < 0:
                first_wait = [price, -price]
            if not second_wait:
                second_wait = [price, first_sell-price]
            else:
                second_wait[0] = price
                if sum(second_wait) < last_first_sell:
                    second_wait = [price, last_first_sell - price]
            if second_wait and sum(second_wait) > profit:
                profit = sum(second_wait)
        if second_wait:
            return max(sum(first_wait), sum(second_wait), first_sell, profit)
        else:
            return max(sum(first_wait), first_sell, profit)


print(Solution().maxProfit([3,2,6,5,0,3]))
print(Solution().maxProfit([3,3,5,0,0,3,1,4]))
print(Solution().maxProfit([1,2,3,4,5]))
print(Solution().maxProfit([7,6,4,3,1]))
