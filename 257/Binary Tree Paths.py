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
        self.result = []

    def makePath(self, node, path):
        if node:
            if node.left is None and node.right is None:
                self.result.append(path + str(node.val))
            if node.left:
                self.makePath(node.left, path + str(node.val) + '->')
            if node.right:
                self.makePath(node.right, path + str(node.val) + '->')

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        if root is None:
            return []
        if root.left is None and root.right is None:
            self.result.append(str(root.val))
        if root.left:
            self.makePath(root.left, str(root.val) + '->')
        if root.right:
            self.makePath(root.right, str(root.val) + '->')
        return self.result
