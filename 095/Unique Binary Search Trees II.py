# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if not n:
            return []
        return self.buildTrees(1, n)

    def buildTrees(self, start, end):
        result = []

        if start > end:
            result.append(None)
            return result

        for i in range(start, end + 1):
            left_child = self.buildTrees(start, i - 1)
            right_child = self.buildTrees(i + 1, end)

            for l in left_child:
                for r in right_child:
                    node = TreeNode(i)
                    node.left = l
                    node.right = r
                    result.append(node)

        return result


print(Solution().generateTrees(0))
