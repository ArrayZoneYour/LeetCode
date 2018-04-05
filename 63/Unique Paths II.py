# /usr/bin/python
# coding: utf-8


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        height = len(obstacleGrid)
        width = len(obstacleGrid[0])
        step_num = [[0 for col in range(width)] for row in range(height)]
        if not obstacleGrid[0][0]:
            step_num[0][0] = 1
        for row in range(1, height):
            if not obstacleGrid[row][0]:
                step_num[row][0] = step_num[row-1][0]
        for col in range(1, width):
            if not obstacleGrid[0][col]:
                step_num[0][col] = step_num[0][col-1]
        for row in range(1, height):
            for col in range(1, width):
                if not obstacleGrid[row][col]:
                    step_num[row][col] = step_num[row-1][col] + step_num[row][col-1]
        return step_num[-1][-1]


print(Solution().uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
]))