# /usr/bin/python
# coding: utf-8


class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        height = len(grid)
        width = len(grid[0])
        step_num = (height + width) - 2
        for step in range(1, step_num+1):
            for row in range(min(step+1, height)):
                col = step - row
                if 0 <= row < height and 0 <= col < width:
                    if not row:
                        grid[row][col] += grid[row][col-1]
                    elif not col:
                        grid[row][col] += grid[row-1][col]
                    else:
                        grid[row][col] += min(grid[row][col-1], grid[row-1][col])
        return grid[-1][-1]


print(Solution().minPathSum([[1,2],[5,6],[1,1]]))
