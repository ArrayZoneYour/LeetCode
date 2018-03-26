# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def _isSymmetric(self, left, right):
        if left is None or right is None:
            return left == right
        else:
            if left.val == right.val:
                return self._isSymmetric(left.right, right.left) and self._isSymmetric(left.left, right.right)
            else:
                return False

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self._isSymmetric(root.left, root.right)

