# /usr/bin/python
# coding: utf-8


class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []
        results = [matrix[0][0]]
        count, total = 1, len(matrix) * len(matrix[0])
        under_boundary = len(matrix) - 1
        right_boundary = len(matrix[0]) - 1
        top_boundary = 0
        left_boundary = 0
        row = 0
        col = 0
        while not (left_boundary > right_boundary or top_boundary > under_boundary):
            if count == total:
                break
            while col < right_boundary:
                col += 1
                results.append(matrix[row][col])
                count += 1
            top_boundary += 1
            if count == total:
                break
            while row < under_boundary:
                row += 1
                results.append(matrix[row][col])
                count += 1
            right_boundary -= 1
            if count == total:
                break
            while col > left_boundary:
                col -= 1
                results.append(matrix[row][col])
                count += 1
            under_boundary -= 1
            if count == total:
                break
            while row > top_boundary:
                row -= 1
                results.append(matrix[row][col])
                count += 1
            left_boundary += 1
        return results


print(Solution().spiralOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]))
print(Solution().spiralOrder([
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]))
print(Solution().spiralOrder([[3],[2]]))
