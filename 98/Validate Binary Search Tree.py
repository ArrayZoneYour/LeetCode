# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidNode(self, node, low_boundary=None, high_boundary=None):
        if node:
            if low_boundary is not None:
                if low_boundary < node.val:
                    if high_boundary is not None:
                        return node.val < high_boundary and \
                               self.isValidNode(node.left, low_boundary, node.val) and \
                               self.isValidNode(node.right, node.val, high_boundary)
                    else:
                        return self.isValidNode(node.left, low_boundary, node.val) and \
                           self.isValidNode(node.right, node.val, high_boundary)
                else:
                    return False
            elif high_boundary is not None:
                    return node.val < high_boundary and \
                           self.isValidNode(node.left, low_boundary, node.val) and \
                           self.isValidNode(node.right, node.val, high_boundary)
        else:
            return True

    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        else:
            return self.isValidNode(root.left, None, root.val) and \
                   self.isValidNode(root.right, root.val, None)
