# /usr/bin/python
# coding: utf-8
import math


class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        past = 0
        candy_nums = 0
        candy_num = 0
        feed_child_num = 0
        feed_head_rate = 0
        for rate in ratings:
            if rate > past:
                candy_num += 1
                candy_nums += candy_num
                feed_child_num = 1
                feed_head_rate = 0
            elif rate < past:
                if feed_head_rate == 0:
                    feed_head_rate = candy_num
                candy_num = 1
                feed_child_num += 1
                candy_nums += feed_child_num + int(feed_head_rate < feed_child_num) - 1
            else:
                candy_nums += 1
                candy_num = 1
                feed_child_num = 1
                feed_head_rate = 0
            past = rate
        return candy_nums


print(Solution().candy([1,3,2,2,1]))
print(Solution().candy([1, 0, 2]))
print(Solution().candy([1, 2, 2]))
print(Solution().candy([1,2,87,87,87,2,1]))
