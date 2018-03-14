# /usr/bin/python
# coding: utf-8

class ListNode():

    def __init__(self, value):
        self.value = value
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        dummyHead = ListNode(0)
        dummyHead.next = head
        pre = dummyHead

        for i in range(m - 1):
            pre = pre.next

        end = None
        cur = pre.next
        for i in range(n - m + 1):
            next = cur.next
            cur.next = end
            end = cur
            cur = next

        pre.next.next = cur
        pre.next = end

        return dummyHead.next
