# /usr/bin/python
# coding: utf-8
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        dic = {}
        h = []
        for num in nums:
            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        for key in dic.keys():
            if len(h) < k:
                heapq.heappush(h, (dic[key], key))
            else:
                minimum = heapq.heappop(h)
                if dic[key] > minimum[0]:
                    heapq.heappush(h, (dic[key], key))
                else:
                    heapq.heappush(h, minimum)
        return [el[1] for el in h]


Solution().topKFrequent([1, 1, 1, 2, 2, 3], 2)
