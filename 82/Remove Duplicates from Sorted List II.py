# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        Given 1->2->3->3->4->4->5, return 1->2->5.
        Given dummy->1->1->1->2->3, return 2->3.
        """
        dummyHead = ListNode(0)
        dummyHead.next = head

        # 以下一个元素作为当前指针
        if not head:
            return head
        cur = head
        if cur.next is None:
            return head
        # 以dummyHead为前一个元素
        pre = dummyHead
        while cur is not None and cur.next is not None:
            # 判断下一个元素和当前元素指针值相同
            if cur.next.val == cur.val:
                # 如果值相同，当前元素的next指针指向next的next，直至不同或者指向空为止
                while cur.next is not None and cur.next.val == cur.val:
                    cur.next = cur.next.next
                # 前一个元素的指针指向当前元素的下一个
                pre.next = cur.next
            # 判断得到下一个元素的值与当前元素指针对应的值不同
            else:
                pre = pre.next
            # 当前指针后移
            cur = cur.next
            # 如果当前元素值或者下一个元素值为None，返回dummyHead.next
        return dummyHead.next


node1 = ListNode(1)
node2 = ListNode(1)
node3 = ListNode(2)
node4 = ListNode(2)
node1.next = node2
node2.next = node3
node3.next = node4
Solution().deleteDuplicates(node1)
print()