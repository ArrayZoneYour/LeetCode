# /usr/bin/python
# coding: utf-8


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def __init__(self):
        self.q = []
        self.result = []

    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            self.q.append(root)
            level = 0
            while self.q:
                size = len(self.q)
                self.result.append([])
                for i in range(size):
                    head = self.q.pop(0)
                    self.result[-1].append(head.val)
                    if head.left:
                        self.q.append(head.left)
                    if head.right:
                        self.q.append(head.right)
                if level % 2:
                    self.result[-1].reverse()
                level += 1
            return self.result
