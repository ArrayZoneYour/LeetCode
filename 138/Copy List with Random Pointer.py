# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if not head:
            return
        head_copy = res = RandomListNode(head.label)
        memo = {head.label: head_copy}
        while head:
            if head.random:
                if head.random.label not in memo:
                    memo[head.random.label] = RandomListNode(head.random.label)
                head_copy.random = memo[head.random.label]
            if head.next:
                if head.next.label not in memo:
                    memo[head.next.label] = RandomListNode(head.next.label)
                head_copy.next = memo[head.next.label]
            head = head.next
            head_copy = head_copy.next
        return res
