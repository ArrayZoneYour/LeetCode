# /usr/bin/python
# coding: utf-8
from collections import deque

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        q = deque([])
        result = []
        if not root:
            return []
        else:
            q.append(root)
            while q:
                size = len(q)
                result.append(q[-1].val)
                for i in range(size):
                    old_el = q.popleft()
                    if old_el.left:
                        q.append(old_el.left)
                    if old_el.right:
                        q.append(old_el.right)
            return result
