# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.result = []

    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.result.append(root.val)
            self.preorderTraversal(root.left)
            self.preorderTraversal(root.right)
        return self.result
