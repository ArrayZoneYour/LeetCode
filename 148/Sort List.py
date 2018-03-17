# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
# 通过自底向上的归并排序实现
# 获取链表的长度，然后以1=>2=>4=>8的顺序进行归并排序直到当前循环要归并需要的单个链表长度超出总长度
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    def merge(self, l, r):
        if not l or not r:
            return l or r
        if l.val > r.val:
            l, r = r, l
        head = cur = l
        l = l.next
        cur.next = None
        while l and r:
            if l.val < r.val:
                cur.next = l
                cur = cur.next
                l = l.next
            else:
                cur.next = r
                cur = cur.next
                r = r.next
        cur.next = l or r
        return head

    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        fast, slow = head.next, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        second = slow.next
        slow.next = None
        l = self.sortList(head)
        r = self.sortList(second)
        return self.merge(l, r)


node1, node2, node3, node4, node5 = ListNode(4), ListNode(2), ListNode(1), ListNode(3), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = None

Solution().sortList(node1)
