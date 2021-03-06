# /usr/bin/python
# coding: utf-8


# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None


class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        tail = dummy = TreeLinkNode(0)
        while root:
            if root.left:
                tail.next = root.left
                tail = tail.next
            else:
                tail.next = None
            if root.right:
                tail.next = root.right
                tail = tail.next
            else:
                tail.next = None
            root = root.next
            if not root:
                tail = dummy
                root = tail.next

