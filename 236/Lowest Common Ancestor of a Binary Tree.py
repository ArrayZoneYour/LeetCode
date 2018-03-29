# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # Tip: Only two nodes, or left+left, or right+right or left+right
        # find the node or has no child, stop
        if root == p or root == q:
            return root
        left = self.lowestCommonAncestor(root.left, p, q) if root.left else None
        right = self.lowestCommonAncestor(root.right, p, q) if root.right else None
        if left:
            # left + right
            if right:
                return root
            # left + left
            return left
        # right + right
        if right:
            return right
