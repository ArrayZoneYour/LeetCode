# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if not head:
            return None
        if not head.next:
            return TreeNode(head.val)
        slow = head
        fast = head
        last_slow = None
        while fast.next and fast.next.next:
            last_slow = slow
            slow = slow.next
            fast = fast.next.next
        node = TreeNode(slow.val)
        if last_slow:
            last_slow.next = None
            node.left = self.sortedListToBST(head)
        node.right = self.sortedListToBST(slow.next)
        return node
