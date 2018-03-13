# /usr/bin/python
# coding: utf-8

import numpy as np  # np.longdouble

# Definition for a point.
class Point:
    def __init__(self, a=0, b=0):
        self.x = a
        self.y = b


class Solution:
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        dic = {}
        if len(points) == 1:
            return 1
        elif len(points) == 0:
            result = 0
        else:
            result = 1
        same = 1
        for index_out, point_out in enumerate(points):
            same = 1
            for index_in, point_in in enumerate(points):
                if index_in == index_out:
                    continue
                if point_in.x == point_out.x:
                    if point_in.y == point_out.y:
                        same += 1
                    elif dic.__contains__('inf'):
                        dic['inf'] += 1
                    else:
                        dic['inf'] = 1
                else:
                    k = (point_out.y - point_in.y) * 1000000000.0 / (point_out.x - point_in.x)
                    if dic.__contains__(k):
                        dic[k] += 1
                    else:
                        dic[k] = 1
            if len(dic) > 0:
                result = max(result, max(dic.values()) + same)
            else:
                return same
            dic = {}
        return result


print(Solution().maxPoints([Point(0, 0), Point(94911151, 94911150), Point(94911152, 94911151)]))
print(Solution().maxPoints([Point(0, 0), Point(1, 0)]))
print(Solution().maxPoints([Point(0, 0), Point(1, 1), Point(1, -1)]))
