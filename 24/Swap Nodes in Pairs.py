# /usr/bin/python
# coding: utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        input： 1->2->3->4
        output：2->1->4->3
        过渡状态：
                dummyHead->2    1->2->3->4
                dummyHead->2->1 (1->2) 3->4
        关键点: 两个为一个单元进行操作，需要有一个指针保存下两个元素的位置
        """
        if head is None:
            return None
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead
        # 如果后面还有两个及两个以上的元素，保存这两个元素的位置
        if cur.next and cur.next.next:
            first = cur.next
        # 更新标志
        flag = False
        _end = dummyHead.next
        # 如果后面还有两个及两个以上的元素，执行循环
        while cur.next and cur.next.next:
            # 将要更新的元素值填入临时变量(可能为空？)
            if first.next.next and first.next.next.next:
                _first = first.next.next
                flag = True
            else:
                _end = first.next.next
                flag = False
            # 当前指针的下一个指向后面的第二个元素
            cur.next = first.next
            # 当前指针后移
            cur = cur.next
            # 当前指针的下一个指向第一个元素
            cur.next = first
            # 当前指针后移
            cur = cur.next
            # 更新两个元素的值
            if flag:
                first = _first
            else:
                cur.next = None
        # 此时只剩下末尾的零个或者一个元素，将当前元素指针指向它即可
        cur.next = _end
        # 返回头部指针
        return dummyHead.next


node1, node2, node3, node4 = ListNode(1), ListNode(2), ListNode(3), ListNode(4)
node1.next = node2
node2.next = node3
node3.next = node4
Solution().swapPairs(node1)
node = ListNode(1)
Solution().swapPairs(node)
node1, node2, node3 = ListNode(1), ListNode(2), ListNode(3)
node1.next = node2
node2.next = node3
Solution().swapPairs(node1)
