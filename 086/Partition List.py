# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        left_list, right_list = ListNode(0), ListNode(0)
        cur_left, cur_right = left_list, right_list
        while head:
            if head.val < x:
                cur_left.next = head
                cur_left = cur_left.next
            else:
                cur_right.next = head
                cur_right = cur_right.next
            head = head.next

        cur_right.next = None
        cur_left.next = right_list.next
        return left_list.next
