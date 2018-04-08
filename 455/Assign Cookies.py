# /usr/bin/python
# coding: utf-8


class Solution:
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        child_num = len(g)
        cookie_num = len(s)
        result = 0
        g.sort()
        s.sort()
        cookie_id = 0
        child_id = 0
        while cookie_id < cookie_num and child_id < child_num:
            if g[child_id] <= s[cookie_id]:
                result += 1
                child_id += 1
            cookie_id += 1
        return result


assert Solution().findContentChildren([1, 2, 3], [1, 1]) == 1
assert Solution().findContentChildren([1, 2], [1, 2, 3]) == 2
assert Solution().findContentChildren([1, 2, 3], [3]) == 1
