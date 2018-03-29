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
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        node_num = len(nums)
        if node_num == 0:
            return None
        if node_num == 1:
            return TreeNode(nums[0])
        center_index = math.ceil(node_num / 2) - 1
        node = TreeNode(nums[center_index])
        node.left = self.sortedArrayToBST(nums[:center_index])
        node.right = self.sortedArrayToBST(nums[center_index+1:])
        return node
