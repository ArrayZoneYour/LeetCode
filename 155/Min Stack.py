# /usr/bin/python
# coding: utf-8


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_vals = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)
        if self.min_vals:
            self.min_vals.append(min(self.min_vals[-1], x))
        else:
            self.min_vals.append(x)

    def pop(self):
        """
        :rtype: void
        """
        if self.stack:
            self.stack.pop()
            self.min_vals.pop()

    def top(self):
        """
        :rtype: int
        """
        if self.stack:
            return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        if self.min_vals:
            return self.min_vals[-1]


# Your MinStack object will be instantiated and called as such:
min_stack = MinStack()
min_stack.push(-2)
min_stack.push(0)
min_stack.push(-3)
print(min_stack.getMin())
min_stack.pop()
print(min_stack.top())
print(min_stack.getMin())
