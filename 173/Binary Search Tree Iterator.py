# /usr/bin/python
# coding: utf-8


# Definition for a  binary tree node
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BSTIterator(object):
    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.iterator_list = [root] if root else []
        while root and root.left:
            root = root.left
            self.iterator_list.append(root)

    def hasNext(self):
        """
        :rtype: bool
        """
        return len(self.iterator_list) > 0

    def next(self):
        """
        :rtype: int
        """
        cur = self.iterator_list.pop()
        val = cur.val
        if cur.right:
            cur = cur.right
            self.iterator_list.append(cur)
            while cur.left:
                cur = cur.left
                self.iterator_list.append(cur)
        return val


# Your BSTIterator will be called like this:
i, v = BSTIterator(TreeNode(1)), []
while i.hasNext(): v.append(i.next())
print(v)
