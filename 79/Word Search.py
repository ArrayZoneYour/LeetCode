# /usr/bin/python
# coding: utf-8


class Solution:

    def findWord(self, row, col, word, board, visited, board_height, board_width):
        # top, right, down, left
        if board[row][col] == word[0]:
            if len(word) == 1:
                return True
            visited[row][col] = True
            if row and not visited[row-1][col]:
                if self.findWord(row-1, col, word[1:], board, visited, board_height, board_width):
                    return True
            if col != board_width-1 and not visited[row][col+1]:
                if self.findWord(row, col+1, word[1:], board, visited, board_height, board_width):
                    return True
            if row != board_height-1 and not visited[row+1][col]:
                if self.findWord(row+1, col, word[1:], board, visited, board_height, board_width):
                    return True
            if col and not visited[row][col-1]:
                if self.findWord(row, col-1, word[1:], board, visited, board_height, board_width):
                    return True
            visited[row][col] = False
        return False

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        board_height = len(board)
        board_width = len(board[0])
        visited = [[False for i in range(board_width)] for j in range(board_height)]
        for row in range(board_height):
            for col in range(board_width):
                if self.findWord(row, col, word, board, visited, board_height, board_width):
                    return True
        return False


print(Solution().exist([
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
], "ABCCE"))
