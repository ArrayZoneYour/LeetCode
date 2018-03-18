# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        Example:
            input: 1->2->3->4->5->NULL, 2
            output: 4->5->1->2->3->NULL
            思路：
            双指针，上面的例子中，当右侧指针移动至5时，左侧指针应当指向3，(右侧指针超前2位)
            然后保存3的下一个元素为返回的头结点，然后把下一个元素置为None，
            右侧指针的下一个元素置为输入头指针
        """
        if head is None or head.next is None:
            return head
        length = 0
        pointer_counter = head
        while pointer_counter:
            length += 1
            pointer_counter = pointer_counter.next
        if k % length == 0:
            return head
        k = k % length
        pointer_l = pointer_r = head
        while k > 0:
            pointer_r = pointer_r.next
            k -= 1
        while pointer_r.next is not None:
            pointer_l = pointer_l.next
            pointer_r = pointer_r.next
        ret_head = pointer_l.next
        pointer_l.next = None
        pointer_r.next = head

        return ret_head


node1, node2, node3, node4, node5 = ListNode(1), ListNode(2), ListNode(3), ListNode(4), ListNode(5)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
Solution().rotateRight(node1, 5)
