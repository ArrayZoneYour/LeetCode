# /usr/bin/python
# coding: utf-8


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dic = {'{': '}', '[': ']', '(': ')'}
        for el in s:
            if el in dic.keys():
                stack.append(el)
            else:
                if not stack:
                    return False
                else:
                    if dic[stack.pop()] != el:
                        return False
        return stack == []


Solution().isValid("{()()}")
