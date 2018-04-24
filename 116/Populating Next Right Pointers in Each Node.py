# /usr/bin/python
# coding: utf-8


# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if root:
            self.inner_connect(root)
            if root.left:
                self.outer_connect(root.left, root.right)
                self.connect(root.left)
                self.connect(root.right)

    def inner_connect(self, root):
        if root.left:
            root.left.next = root.right

    def outer_connect(self, left_node, right_node):
        cur_l, cur_r = left_node, right_node
        while cur_l.right:
            cur_l.right.next = cur_r.left
            cur_l = cur_l.right
            cur_r = cur_r.left
