# /usr/bin/python
# coding: utf-8


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger(object):
   def isInteger(self):
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       :rtype bool
       """

   def getInteger(self):
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       :rtype int
       """

   def getList(self):
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       :rtype List[NestedInteger]
       """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.stack = []

    def collect_el(self, nestedList):
        if nestedList.isInteger():
            self.stack.append(nestedList.getInteger())
        else:
            for el in nestedList.getList():
                self.collect_el(el)


    def next(self):
        """
        :rtype: int
        """
        res = self.stack[0]
        del self.stack[0]
        return res

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.stack:
            return True

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
