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
        self.node_num = 0

    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root:
            self.node_num += 1
            self.countNodes(root.left)
            self.countNodes(root.right)
        return self.node_num
