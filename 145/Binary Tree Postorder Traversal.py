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

    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root:
            self.postorderTraversal(root.left)
            self.postorderTraversal(root.right)
            self.result.append(root.val)
        return self.result
