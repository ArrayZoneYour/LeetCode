# /usr/bin/python
# coding: utf-8


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        将数字依次压入栈中，遇到运算符时做弹栈操作
        """
        stack = []
        for token in tokens:
            if (token.startswith('-') and token[1:] or token).isnumeric():
                stack.append(int(token))
            else:
                first, second = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(second + first)
                elif token == '-':
                    stack.append(second - first)
                elif token == '*':
                    stack.append(second * first)
                else:
                    stack.append(int(operator.truediv(second, first)))
        return stack.pop()


Solution().evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"])
Solution().evalRPN(["4", "13", "5", "/", "+"])
