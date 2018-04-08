# /usr/bin/python
# coding: utf-8


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: int
        """
        if not intervals:
            return 0
        intervals.sort(key=lambda interval: (interval.end, interval.start))
        erase_num = 0
        low_boundary = intervals[0].start
        for interval in intervals:
            if interval.start >= low_boundary:
                low_boundary = interval.end
            else:
                erase_num += 1
        return erase_num
