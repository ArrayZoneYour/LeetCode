# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        将给定链表切分为两部分，翻转后半部分的链表，然后逐个比较两个链表的元素
        """
        if head is None:
            return None
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        slow = slow.next
        pre = None
        nex = slow
        while slow:
            nex = nex.next
            slow.next = pre
            pre = slow
            slow = nex
        while pre:
            if pre.val == head.val:
                pre, head = pre.next, head.next
            else:
                return False
        return True


node1, node2, node3, node4, node5 = ListNode(1), ListNode(1), ListNode(3), ListNode(2), ListNode(1)
node1.next = node2
node2.next = None
node3.next = node4
node4.next = node5
Solution().isPalindrome(node1)
