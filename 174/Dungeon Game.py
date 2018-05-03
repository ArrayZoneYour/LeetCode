# /usr/bin/python
# coding: utf-8


class Solution(object):
    def calculateMinimumHP(self, dungeon):
        """
        :type dungeon: List[List[int]]
        :rtype: int
        """
        width = len(dungeon[0])
        height = len(dungeon)
        dungeon[-1][-1] = max(1 - dungeon[-1][-1], 1)
        for i in range(2, width + 1):
            dungeon[-1][-i] = max(1, dungeon[-1][-i+1] - dungeon[-1][-i])
        for i in range(2, height + 1):
            dungeon[-i][-1] = max(1, dungeon[-i+1][-1] - dungeon[-i][-1])
        for row in range(2, height + 1):
            for col in range(2, width + 1):
                dungeon[-row][-col] = min(dungeon[-row+1][-col] - dungeon[-row][-col], dungeon[-row][-col+1] - dungeon[-row][-col])
                dungeon[-row][-col] = max(1, dungeon[-row][-col])
        return dungeon[0][0]


print(Solution().calculateMinimumHP([[-2,-3,3],[-5,-10,1],[10,30,-5]]))
