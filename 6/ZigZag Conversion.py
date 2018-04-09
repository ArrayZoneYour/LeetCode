# /usr/bin/python
# coding: utf-8


class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        period_num = numRows + numRows - 2
        result_set = [[] for i in range(numRows)]
        for index, el in enumerate(s):
            row = index % period_num
            if row < numRows:
                result_set[row].append(el)
            else:
                result_set[period_num - row].append(el)
        result = ''
        for i in range(0, len(result_set)):
            result += ''.join(result_set[i])
        return result


print(Solution().convert("PAYPALISHIRING", 4))
