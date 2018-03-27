# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findPath(self, node, sum, path, res):
        path.append(node.val)
        if node.left is None and node.right is None and node.val == sum:
            res.append(path.copy())
        else:
            if node.left:
                self.findPath(node.left, sum - node.val, path, res)
            if node.right:
                self.findPath(node.right, sum - node.val, path, res)
        path.pop()

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        res = []
        path = []
        if root is None:
            return res
        else:
            path.append(root.val)
            if root.left is None and root.right is None and root.val == sum:
                res.append(path.copy())
                return res
            if root.left:
                self.findPath(root.left, sum - root.val, path, res)
            if root.right:
                self.findPath(root.right, sum - root.val, path, res)
        return res
