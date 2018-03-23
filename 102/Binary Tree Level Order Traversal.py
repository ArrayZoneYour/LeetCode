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

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        else:
            self.q.append([root, 0])
            self.levelScan()
            return self.result

    def levelScan(self):
        if self.q:
            new_el = self.q.pop(0)
            if new_el[1] == len(self.result):
                self.result.append([])
            self.result[new_el[1]].append(new_el[0].val)
            if new_el[0].left:
                self.q.append([new_el[0].left, new_el[1] + 1])
            if new_el[0].right:
                self.q.append([new_el[0].right, new_el[1] + 1])
            self.levelScan()
