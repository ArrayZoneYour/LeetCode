# /usr/bin/python
# coding: utf-8


class Solution:
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if not amount:
            return 0
        if not coins:
            return -1
        fill_list = [0] * (amount+1)
        for coin in coins:
            if coin <= amount:
                fill_list[coin] = 1
                for index in range(coin+1, amount+1):
                    if fill_list[index-coin]:
                        fill_list[index] = fill_list[index-coin] + 1 if not fill_list[index] \
                            else min(fill_list[index], fill_list[index-coin] + 1)
        return -1 if not fill_list[-1] else fill_list[-1]


print(Solution().coinChange([2], 1))
