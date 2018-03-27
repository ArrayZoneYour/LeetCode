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
        self.path_nums = []

    def findPathNumber(self, node, cur_num):
        cur_num = cur_num * 10 + node.val
        if node.left is None and node.right is None:
            self.path_nums.append(cur_num)
        else:
            if node.left:
                self.findPathNumber(node.left, cur_num)
            if node.right:
                self.findPathNumber(node.right, cur_num)
        cur_num //= 10

    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        else:
            cur_num = root.val
            if root.left is None and root.right is None:
                return cur_num
            if root.left:
                self.findPathNumber(root.left, cur_num)
            if root.right:
                self.findPathNumber(root.right, cur_num)
        return sum(self.path_nums)
