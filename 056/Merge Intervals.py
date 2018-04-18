# /usr/bin/python
# coding: utf-8


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        intervals.sort(key=lambda s: s.start)
        index = 0
        length = len(intervals) - 1
        while index < length:
            if intervals[index].end >= intervals[index+1].start:
                if intervals[index+1].end >= intervals[index].end:
                    intervals[index].end = intervals[index+1].end
                del intervals[index+1]
                length -= 1
            else:
                index += 1
        return intervals

