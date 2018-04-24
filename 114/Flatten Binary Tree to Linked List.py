# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        head_l, tail_l = self.connect_head_and_tail(root.left)
        head_r, tail_r = self.connect_head_and_tail(root.right)
        if head_l:
            root.left, root.right = None, head_l
            if head_r:
                tail_l.left, tail_l.right = None, head_r
        else:
            root.left, root.right = None, head_r

    def connect_head_and_tail(self, root):
        if not root:
            return None, None
        if not root.left and not root.right:
            return root, root
        head_l, tail_l = self.connect_head_and_tail(root.left)
        head_r, tail_r = self.connect_head_and_tail(root.right)
        if head_l:
            root.left, root.right = None, head_l
            if head_r:
                tail_l.left, tail_l.right = None, head_r
                return root, tail_r
            return root, tail_l
        else:
            root.left, root.right = None, head_r
            return root, tail_r
