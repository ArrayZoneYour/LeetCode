# /usr/bin/python
# coding: utf-8
import math


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def __init__(self):
        self.max_sum = -math.inf

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self._maxPathSum(root)
        return self.max_sum

    def _maxPathSum(self, root):
        if not root.left and not root.right:
            self.max_sum = max(root.val, self.max_sum)
            return root.val
        if root.left and root.right:
            left_sum = self._maxPathSum(root.left)
            right_sum = self._maxPathSum(root.right)
            if root.val > 0:
                if left_sum > 0 and right_sum > 0:
                    self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
                else:
                    self.max_sum = max(self.max_sum, root.val + max(left_sum, right_sum, 0))
            else:
                if left_sum + root.val > 0 and left_sum + right_sum > 0:
                    self.max_sum = max(self.max_sum, root.val + left_sum + right_sum)
                else:
                    self.max_sum = max(self.max_sum, max(root.val, left_sum, right_sum))
            return root.val + max(left_sum, right_sum, 0)
        elif root.left:
            left_sum = self._maxPathSum(root.left)
            if root.val > 0:
                if root.val + max(left_sum, 0) > self.max_sum:
                    self.max_sum = root.val + max(left_sum, 0)
            else:
                if max(root.val, left_sum) > self.max_sum:
                    self.max_sum = max(root.val, left_sum)
            return root.val + max(left_sum, 0)
        else:
            right_sum = self._maxPathSum(root.right)
            if root.val > 0:
                if root.val + max(right_sum, 0) > self.max_sum:
                    self.max_sum = root.val + max(right_sum, 0)
            else:
                if max(root.val, right_sum) > self.max_sum:
                    self.max_sum = max(root.val, right_sum)
            return root.val + max(right_sum, 0)


root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.right.right.right = TreeNode(1)
print(Solution().maxPathSum(root))
