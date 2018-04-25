# /usr/bin/python
# coding: utf-8


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        pre = [1]
        for width in range(1, rowIndex+1):
            cur = [1]
            for j in range(1, width):
                cur.append(pre[j-1] + pre[j])
            cur.append(1)
            pre = cur
        return pre


print(Solution().getRow(4))
