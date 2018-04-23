# /usr/bin/python
# coding: utf-8
import math


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.abnormal_element = []
        self.pre = TreeNode(-math.inf)

    def find_abnormal_list(self, root):
        if not root:
            return
        self.find_abnormal_list(root.left)
        if root.val < self.pre.val:
            if not self.abnormal_element:
                self.abnormal_element = [self.pre, root]
            else:
                self.abnormal_element[1] = root
        self.pre = root
        self.find_abnormal_list(root.right)

    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.find_abnormal_list(root)
        self.abnormal_element[0].val, self.abnormal_element[1].val = \
            self.abnormal_element[1].val, self.abnormal_element[0].val

