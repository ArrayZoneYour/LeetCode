# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.sum = 0

    def leftNodeProcess(self, node):
        if node:
            if node.left is None and node.right is None:
                self.sum += node.val
            else:
                self.leftNodeProcess(node.left)
                self.sumOfLeftLeaves(node.right)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        self.leftNodeProcess(root.left)
        self.sumOfLeftLeaves(root.right)
        return self.sum

