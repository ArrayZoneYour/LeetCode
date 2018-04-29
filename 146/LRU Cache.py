# /usr/bin/python
# coding: utf-8


class LinkedList:

    def __init__(self, value, label):
        self.val = value
        self.label = label
        self.next = None


class LRUCache:

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.size = 1
        self.head = LinkedList(0, -1)
        self.tail = self.head
        self.hash_table = {-1: self.head}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.hash_table:
            if self.hash_table[key] is not self.tail:
                new_tail = LinkedList(self.hash_table[key].val, key)
                self.tail.next = new_tail
                self.tail = self.tail.next
                del_node = self.hash_table[key]
                del_node.val = del_node.next.val
                del_node.label = del_node.next.label
                del_node.next = del_node.next.next
                self.hash_table[key] = self.tail
                self.hash_table[del_node.label] = del_node
            return self.tail.val
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self.hash_table:
            self.hash_table[key].val = value
            self.get(key)
        else:
            if self.size == self.capacity:
                del self.hash_table[self.head.label]
            self.tail.next = LinkedList(value, key)
            self.tail = self.tail.next
            self.hash_table[key] = self.tail
            if self.size == self.capacity:
                self.head = self.head.next
            else:
                self.size += 1


# Your LRUCache object will be instantiated and called as such:
cache = LRUCache(2)
cache.put(2, 1)
cache.put(2, 2)
print(cache.get(2))
cache.put(1, 1)
cache.put(4, 1)
print(cache.get(2))
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
