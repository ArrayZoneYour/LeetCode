# /usr/bin/python
# coding: utf-8


class Solution:

    def floodfill(self, row, col, grid, visited, grid_width, grid_height):
        visited[row][col] = True
        if row != grid_height - 1 and not visited[row+1][col] and grid[row+1][col] == "1":
            self.floodfill(row+1, col, grid, visited, grid_width, grid_height)
        if col != grid_width - 1 and not visited[row][col+1] and grid[row][col+1] == "1":
            self.floodfill(row, col+1, grid, visited, grid_width, grid_height)
        if col and not visited[row][col-1] and grid[row][col-1] == "1":
            self.floodfill(row, col-1, grid, visited, grid_width, grid_height)
        if row and not visited[row-1][col] and grid[row-1][col] == "1":
            self.floodfill(row-1, col, grid, visited, grid_width, grid_height)

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if not grid:
            return 0
        island_num = 0
        grid_height = len(grid)
        grid_width = len(grid[0])
        visited = [[False for i in range(grid_width)] for j in range(grid_height)]
        for row in range(grid_height):
            for col in range(grid_width):
                if not visited[row][col] and grid[row][col] == "1":
                    self.floodfill(row, col, grid, visited, grid_width, grid_height)
                    island_num += 1
                else:
                    visited[row][col] = True
        return island_num

