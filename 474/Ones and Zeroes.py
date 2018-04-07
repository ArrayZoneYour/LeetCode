# /usr/bin/python
# coding: utf-8
import time


class Solution:
    def findMaxForm(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        dic = {}
        board = [[0 for x in range(m+1)] for y in range(n+1)]
        for s in strs:
            x = s.count('0')
            y = s.count('1')
            if (x, y) in dic:
                dic[(x, y)] += 1
            else:
                dic[(x, y)] = 1
        for (x, y) in dic.keys():
            if dic[(x, y)] > 100 // max(x, y):
                dic[(x, y)] = 100 // max(x, y)
        for (x, y) in dic.keys():
            for i in range(dic[(x, y)]):
                for n_row in range(n-y+1):
                    row = n - n_row
                    for n_col in range(m-x+1):
                        col = m - n_col
                        board[row][col] = board[row][col] \
                            if board[row][col] > board[row-y][col-x] else board[row-y][col-x] + 1

        return board[-1][-1]


print(Solution().findMaxForm(["10", "0", "1"], 1, 1))
start = time.time()
print(Solution().findMaxForm(["1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101"], 100, 100))
end = time.time()
print(len(["1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101","1101","0101"]))
print(str(end - start))
