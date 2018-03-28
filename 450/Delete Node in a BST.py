# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def getNode(self, root, value):
        if root is None:
            return None
        if root.val > value:
            return self.getNode(root.left, value)
        if root.val < value:
            return self.getNode(root.right, value)
        return root

    def deleteMaxLevelNode(self, root, value):
        if root.val > value:
            if root.left.val == value:
                root.left = None
            else:
                self.deleteMaxLevelNode(root.left, value)
        if root.val < value:
            if root.right.val == value:
                root.right = None
            else:
                self.deleteMaxLevelNode(root.right, value)

    def getNearestBiggerNode(self, root):
        root = root.right
        while root.left:
            root = root.left
        return root

    def deleteNearestBiggerNode(self, root):
        if root.right.left is None:
            root.right = root.right.right
        else:
            root = root.right
            while root.left.left:
                root = root.left
            root.left = root.left.right

    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        # The solution is search the value nearest to the root.val to replace the node to delete
        # Step 1: get the node to delete
        # Step 2: search the node whose value is nearest to the node.val
        # if you search the node in the right child tree(right child tree exist),
        # delete_node.val <= replace_node.val;replace_node = None; replace_node.right = delete_node.right
        node = self.getNode(root, key)
        if node is None:
            return root
        if root.left is None and root.right is None:
            return []
        if node.left is None:
            if node.right is None:
                self.deleteMaxLevelNode(root, key)
            else:
                node.val = node.right.val
                node.left = node.right.left
                node.right = node.right.right
        else:
            if node.right is None:
                node.val = node.left.val
                node.right = node.left.right
                node.left = node.left.left
            else:
                replace_node = self.getNearestBiggerNode(node)
                self.deleteNearestBiggerNode(node)
                node.val = replace_node.val
        return root
