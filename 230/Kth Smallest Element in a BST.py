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
        self.k = 0
        self.result = None

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if root.left and self.k < k:
            self.kthSmallest(root.left, k)
        self.k += 1
        if self.k == k:
            self.result = root.val
        if root.right and self.k < k:
            self.kthSmallest(root.right, k)
        return self.result
