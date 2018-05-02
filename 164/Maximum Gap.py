# /usr/bin/python
# coding: utf-8
import math
import bisect


class Solution:
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length < 2:
            return 0
        result = 0
        maximum = minimum = nums[0]
        for num in nums:
            maximum = max(maximum, num)
            minimum = min(minimum, num)
        if maximum == minimum:
            return 0
        step = math.ceil((maximum - minimum) / length)
        buckets = [[] for i in range(length + 1)]
        for num in nums:
            bucket_num = int(math.floor((num - minimum) / step))
            bisect.insort(buckets[bucket_num], num)
        pre = minimum
        for bucket in buckets:
            while bucket:
                cur = bucket.pop(0)
                result = max(cur - pre, result)
                pre = cur
        return result


print(Solution().maximumGap([1, 3, 100]))
print(Solution().maximumGap([3,6,9,1]))
print(Solution().maximumGap([10]))
print(Solution().maximumGap([10, 34, 33, 78, 100]))
print(Solution().maximumGap([1, 1, 1, 1]))
