# /usr/bin/python
# coding: utf-8


# 解法一：查找表
class Solution:
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        dic = {}
        result = 0
        same_dis_num = 0
        for i in range(len(points)):
            for j in range(len(points)):
                if i == j:
                    continue
                distance = (points[j][0] - points[i][0]) * (points[j][0] - points[i][0]) + \
                           (points[j][1] - points[i][1]) * (points[j][1] - points[i][1])
                if dic.__contains__(distance):
                    dic[distance] += 1
                else:
                    dic[distance] = 1
            for same_dis_num in dic.values():
                result += same_dis_num * (same_dis_num - 1)
            dic = {}
        return result


print(Solution().numberOfBoomerangs([[1,1],[2,2],[3,3],[4,4],[5,5],[6,6],[7,7],[8,8]]) == 24)
print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [2, 0]]) == 2)
print(Solution().numberOfBoomerangs([[0, 0], [1, 0], [-1, 0], [0, 1], [0, -1]]) == 20)
