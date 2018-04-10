# /usr/bin/python
# coding: utf-8


class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        example:
        "/home/" => "/home"
        "/a/./b/../../c" => "/c"
        """
        # 用split切分后从左到右依次装入栈中，如果遇到 .. 则推出目前栈顶的元素 . 则不做任何处理
        stack = []
        els = path.split('/')
        for el in els:
            if not el or el == '.':
                continue
            elif el == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(el)
        return '/' + '/'.join(stack)


assert Solution().simplifyPath('/home/') == '/home'
assert Solution().simplifyPath('/a/./b/../../c/') == '/c'
