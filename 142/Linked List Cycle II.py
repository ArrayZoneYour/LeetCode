# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return
        flag_count = False
        count = 0
        slow = head
        fast = head.next
        while fast.next and fast.next.next:
            if slow is fast:
                if flag_count:
                    break
                flag_count = True
            if flag_count:
                count += 1
            slow = slow.next
            fast = fast.next.next
        if not flag_count:
            return
        slow = head
        fast = head
        for i in range(count):
            fast = fast.next
        while not slow is fast:
            slow = slow.next
            fast = fast.next
        return slow


head = ListNode(1)
head.next = ListNode(2)
head.next.next = head
print(Solution().detectCycle(head))
