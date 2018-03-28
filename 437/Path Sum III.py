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
        self.path_num = 0
        self.sum = None

    def findPath(self, root, sum):
        if root.val == sum:
            self.path_num += 1
        if root.left:
            self.findPath(root.left, sum - root.val)
        if root.right:
            self.findPath(root.right, sum - root.val)

    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root is None:
            return 0
        else:
            self.sum = sum
            if root.val == sum:
                self.path_num += 1
            if root.left:
                self.pathSum(root.left, self.sum)
                self.findPath(root.left, sum - root.val)
            if root.right:
                self.pathSum(root.right, self.sum)
                self.findPath(root.right, sum - root.val)
        return self.path_num
