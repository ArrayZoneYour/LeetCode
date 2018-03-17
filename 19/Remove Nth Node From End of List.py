# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        dummyHead = ListNode(0)
        dummyHead.next = head
        # 创建两个指针，间隔为k，当右侧指针到达末尾None的时候，左侧指针为倒数第n个的前一个元素，即需要右侧指针超前n+1位
        cur = fast = dummyHead
        for i in range(n+1):
            fast = fast.next
        while fast:
            fast = fast.next
            cur = cur.next
        cur.next = cur.next.next
        return dummyHead.next


node1, node2, node3, node4, node5 = ListNode(4), ListNode(2), ListNode(1), ListNode(3), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution().removeNthFromEnd(node1, 1)