# /usr/bin/python
# coding: utf-8


class ListNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None
        self.parent = None
        self.pre = None
        self.next = None


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.top_node = None
        self.min_node = None
        self.root = None

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.root:
            self.top_node = self.min_node = self.root = ListNode(x)
        else:
            node = self.root
            while node:
                if node.val == x:
                    node.count += 1
                elif node.val >= x:
                    if node.left:
                        node = node.left
                    else:
                        node.left = ListNode(x)
                        node.left.parent = node
                        if node is self.min_node:
                            self.min_node = node.left
                        self.top_node.next = node.left
                        self.top_node, self.top_node.pre = node.left, self.top_node
                        break
                else:
                    if node.right:
                        node = node.right
                    else:
                        node.right = ListNode(x)
                        node.right.parent = node
                        self.top_node.next = node.right
                        self.top_node, self.top_node.pre = node.right, node
                        break

    def pop(self):
        """
        :rtype: void
        """
        self.top_node.pre.next = self.top_node.next
        self.top_node = self.top_node.next
        if self.root is self.min_node:
            self.root = self.root.right
            node = self.root
            while node.left:
                node = node.left
            self.min_node = node
        else:
            if self.min_node.right:
                self.min_node.parent.left, self.min_node.right.parent = \
                    self.min_node.right, self.min_node.parent
            else:
                self.min_node = self.min_node.parent

    def top(self):
        """
        :rtype: int
        """
        return self.top_node.val

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_node.val


# Your MinStack object will be instantiated and called as such:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-1)
print(min_stack.getMin())
print(min_stack.top())
min_stack.pop()
print(min_stack.getMin())
