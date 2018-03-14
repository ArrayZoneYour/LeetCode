# /usr/bin/python
# coding: utf-8

import collections

class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int  ---最大间隔
        :type t: int  ---最大差值
        :rtype: bool
        """
        if k < 1 or t < 0:
            return False
        dic = collections.OrderedDict()
        for num in nums:
            key = num if not t else num // t  # 如果t为0不需要处理，否则需要缩放k倍
            for el in (dic.get(key - 1), dic.get(key), dic.get(key + 1)):
                if el is not None and abs(num - el) <= t:
                    return True
            if len(dic) == k:
                dic.popitem(False)
            dic[key] = num
        return False


print(Solution().containsNearbyAlmostDuplicate([1, 2], 0, 1) is False)
