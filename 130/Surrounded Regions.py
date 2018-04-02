# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.board_height = 0
        self.board_width = 0

    def floodfill(self, row, col, visited, board):
        visited[row][col] = True
        if row and not visited[row-1][col] and board[row-1][col] == 'O':
            self.floodfill(row-1, col, visited, board)
        if col != self.board_width-1 and not visited[row][col+1] and board[row][col+1] == 'O':
            self.floodfill(row, col+1, visited, board)
        if row != self.board_height-1 and not visited[row+1][col] and board[row+1][col] == 'O':
            self.floodfill(row+1, col, visited, board)
        if col and not visited[row][col-1] and board[row][col-1] == 'O':
            self.floodfill(row, col-1, visited, board)

    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        self.board_height = len(board)
        self.board_width = len(board[0])
        visited = [[False for i in range(self.board_width)] for j in range(self.board_height)]
        for row in range(self.board_height):
            if not visited[row][0] and board[row][0] == 'O':
                self.floodfill(row, 0, visited, board)
            if not visited[row][-1] and board[row][-1] == 'O':
                self.floodfill(row, self.board_width-1, visited, board)
        for col in range(self.board_width):
            if not visited[0][col] and board[0][col] == 'O':
                self.floodfill(0, col, visited, board)
            if not visited[-1][col] and board[-1][col] == 'O':
                self.floodfill(self.board_height-1, col, visited, board)
        for row in range(self.board_height):
            for col in range(self.board_width):
                if not visited[row][col] and board[row][col] == 'O':
                    board[row][col] = 'X'


print(Solution().solve([["X","O","O","O","X","O","O"],["O","X","O","O","O","O","O"],["O","O","O","O","O","O","O"],["O","O","O","X","O","O","O"],["X","O","O","X","X","O","X"],["O","X","O","O","O","O","X"],["O","O","O","X","O","O","O"]]))