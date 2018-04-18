# /usr/bin/python
# coding: utf-8


class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        result = [[0 for i in range(n)] for j in range(n)]
        count, total = 1, n * n
        top_boundary, left_boundary = 0, 0
        under_boundary, right_boundary = n-1, n-1
        row, col = 0, 0
        result[0][0] = 1
        while count < total:
            while col < right_boundary:
                count += 1
                col += 1
                result[row][col] = count
            if count == total:
                break
            top_boundary += 1
            while row < under_boundary:
                count += 1
                row += 1
                result[row][col] = count
            right_boundary -= 1
            if count == total:
                break
            while col > left_boundary:
                count += 1
                col -= 1
                result[row][col] = count
            under_boundary -= 1
            if count == total:
                break
            while row > top_boundary:
                count += 1
                row -= 1
                result[row][col] = count
            left_boundary += 1
        return result


print(Solution().generateMatrix(3))
print(Solution().generateMatrix(4))
