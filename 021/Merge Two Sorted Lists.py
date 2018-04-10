# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        Input: 1->2->4, 1->3->4
        过渡：dummy->1->1->2->...
        Output: 1->1->2->3->4->4
        注意处理新链表链接新的元素时，该元素所处的头节点的更新
        """
        # 创建虚拟头节点
        dummyHead = ListNode(0)
        cur = dummyHead
        # 保存两个链表的头节点
        # 两个链表的头节点不为None(循环条件)
        while l1 is not None and l2 is not None:
            # 两个头节点都不为None，是否l1头结点的值更大
            if l1.val < l2.val:
                # l1节点的值更大，l1的头结点更新为下一个元素
                tmp = l1
                l1 = l1.next
                # dummyNode所在的链表的下一个元素指向l1节点，更新当前节点为l1节点
                cur.next = tmp
            else:
                tmp = l2
                l2 = l2.next
                cur.next = tmp
            cur = cur.next
        # 如果某一头结点为None，直接将dummyNode所在链表的下一个元素设置为另一个链表
        if l1 is None:
            cur.next = l2
        else:
            cur.next = l1
        return dummyHead.next

head1 = ListNode(1)
node11 = ListNode(2)
node12 = ListNode(4)
head2 = ListNode(1)
node21 = ListNode(3)
node22 = ListNode(4)
head1.next = node11
node11.next = node12
head2.next = node21
node21.next = node22
Solution().mergeTwoLists(head1, head2)
