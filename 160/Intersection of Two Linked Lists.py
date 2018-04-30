# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        curA, curB = headA, headB
        length_a = length_b = 0
        while curA:
            length_a += 1
            curA = curA.next
        while curB:
            length_b += 1
            curB = curB.next
        if length_a > length_b:
            for i in range(length_a - length_b):
                headA = headA.next
        else:
            for i in range(length_b - length_a):
                headB = headB.next
        while headA:
            if headA is headB:
                return headA
            headA, headB = headA.next, headB.next
