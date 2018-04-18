# /usr/bin/python
# coding: utf-8
import math


# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

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

    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        if not intervals:
            return [newInterval]
        left_index = 0
        right_index = len(intervals)
        if newInterval.start <= intervals[0].start:
            intervals.insert(0, newInterval)
        elif newInterval.start >= intervals[-1].start:
            intervals.append(newInterval)
        else:
            while left_index < right_index:
                mid_index = math.floor((left_index + right_index) / 2)
                if intervals[mid_index].start >= newInterval.start:
                    right_index = mid_index
                elif intervals[mid_index].start < newInterval.start:
                    left_index = mid_index
                if intervals[mid_index].start == newInterval.start:
                    intervals.insert(mid_index, newInterval)
                if left_index + 1 == right_index:
                    if newInterval.start <= intervals[left_index].start:
                        intervals.insert(left_index, newInterval)
                    else:
                        intervals.insert(right_index, newInterval)
                    break
        return self.merge(intervals)
