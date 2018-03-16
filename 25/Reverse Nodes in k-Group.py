# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:

    # 翻转长度为k的链表并返回尾结点(注意返回的链表中尾结点还连接着第二个节点)
    def reverseKChild(self, head, k):
        # 遍历第一遍，查看元素是否有k个，没有k个的话不需要翻转链表，直接返回尾结点即可
        check = head
        for i in range(k-1):
            if check.next is None:
                return head, check, False, None
            else:
                check = check.next
        next_head = check.next
        # 翻转链表
        pre = head
        cur = head.next
        next = cur
        for i in range(k-1):
            next = next.next
            cur.next = pre
            pre = cur
            cur = next
        return pre, head, True, next_head


    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        input: 1->2->3->4->5
        k = 2: 2->1->4->3->5
        k = 3: 3->2->1->4->5
        """

        # 创建虚拟头结点
        if head is None:
            return None
        if k == 1:
            return head
        dummyHead = ListNode(0)

        head, tail, flag, next_head = self.reverseKChild(head, k)
        dummyHead.next = head
        while flag and next_head:
            last_tail = tail
            head, tail, flag, next_head = self.reverseKChild(next_head, k)
            last_tail.next = head
        tail.next = None
        return dummyHead.next



node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# Solution().reverseKChild(node1, 3)
# Solution().reverseKGroup(node1, 2)
Solution().reverseKGroup(node1, 3)
