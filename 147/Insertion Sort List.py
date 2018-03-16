# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = head
        if head is None or head.next is None:
            return head
        # 进行n次循环直至可以按大小循环至末尾，每次把第n个元素摆放到正确的位置
        while cur.next is not None:
            if cur.val < cur.next.val:
                cur = cur.next
                continue
            else:
                insert_point_l = dummyHead
                while insert_point_l.next.val < cur.next.val:
                    insert_point_l = insert_point_l.next
                insert_point_r = insert_point_l.next
                insert_point_l.next = cur.next
                cur.next = cur.next.next
                insert_point_l.next.next = insert_point_r
        return dummyHead.next


node1, node2, node3, node4, node5 = ListNode(1), ListNode(7), ListNode(3), ListNode(8), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution().insertionSortList(node1)
