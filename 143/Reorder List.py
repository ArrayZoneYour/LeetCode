# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        Given {1,2,3,4}, reorder it to {1,4,2,3}.
            {1, 2, 3, 4, 5}
        把链表分割为两部分，part_right<=part_l<=part_r+1
        """
        if head is None or head.next is None:
            return
        fast, slow = head.next, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        # 翻转后面的链表：slow下一位开始
        cur = slow.next
        slow.next = None
        pre = None
        nex = cur
        while cur:
            nex = nex.next
            cur.next = pre
            pre = cur
            cur = nex
        # 此时pre为后面链表的头指针，前面的头指针为head，两个轮流取出即可
        dummyHead = ListNode(0)
        cur = dummyHead
        while head:
            cur.next = head
            cur = cur.next
            head = head.next
            cur.next = pre
            cur = cur.next
            if pre:
                pre = pre.next


node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution().reorderList(node1)
