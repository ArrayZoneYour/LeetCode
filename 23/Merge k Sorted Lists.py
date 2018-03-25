# /usr/bin/python
# coding: utf-8

import heapq
# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        h = []
        dummyHead = ListNode(0)
        cur = dummyHead
        for idx, listNode in enumerate(lists):
            # 遍历lists将首元素填入堆当中
            if listNode:
                heapq.heappush(h, (listNode.val, idx, listNode))
        # 弹出堆中最小的元素，并且将该元素的后继加入堆中（如果后继存在）
        while h:
            head = heapq.heappop(h)
            cur.next = head[2]
            cur = cur.next
            if head[2].next:
                heapq.heappush(h, (head[2].next.val, head[1], head[2].next))
        return dummyHead.next
