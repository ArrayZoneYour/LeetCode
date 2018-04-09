# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = l1
        full = 0
        while l1.next and l2.next:
            l1.val += l2.val + full
            full = l1.val // 10
            l1.val = l1.val % 10
            l1, l2 = l1.next, l2.next
        l1.val += l2.val + full
        if l2.next:
            l1.next = l2.next
        while l1.next:
            l1.next.val += l1.val // 10
            l1.val = l1.val % 10
            l1 = l1.next
        if l1.val >= 10:
            l1.val = l1.val - 10
            l1.next = ListNode(1)
        return dummyHead.next
