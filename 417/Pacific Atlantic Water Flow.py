# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.matrix_height = 0
        self.matrix_width = 0
        self.matrix = []

    def floodfill(self, row, col, visited):
        visited[row][col] = True
        if row and not visited[row-1][col] and self.matrix[row][col] <= self.matrix[row-1][col]:
            self.floodfill(row-1, col, visited)
        if col != self.matrix_width-1 and not visited[row][col+1] and self.matrix[row][col] <= self.matrix[row][col+1]:
            self.floodfill(row, col+1, visited)
        if row != self.matrix_height-1 and not visited[row+1][col] and self.matrix[row][col] <= self.matrix[row+1][col]:
            self.floodfill(row+1, col, visited)
        if col and not visited[row][col-1] and self.matrix[row][col] <= self.matrix[row][col-1]:
            self.floodfill(row, col-1, visited)

    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if not matrix:
            return []
        results = []
        self.matrix_height = len(matrix)
        self.matrix_width = len(matrix[0])
        self.matrix = matrix
        visited_p = [[False for i in range(self.matrix_width)] for j in range(self.matrix_height)]
        visited_a = [[False for i in range(self.matrix_width)] for j in range(self.matrix_height)]
        for row in range(self.matrix_height):
            self.floodfill(row, 0, visited_p)
            self.floodfill(row, self.matrix_width-1, visited_a)
        for col in range(self.matrix_width):
            self.floodfill(0, col, visited_p)
            self.floodfill(self.matrix_height-1, col, visited_a)
        for row in range(self.matrix_height):
            for col in range(self.matrix_width):
                if visited_a[row][col] and visited_p[row][col]:
                    results.append([row, col])
        return results
