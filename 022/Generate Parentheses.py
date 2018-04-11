# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.results = []

    def _generateParenthesis(self, left, right, result):
        if not right:
            self.results.append(''.join(result))
        elif not left:
            result.append(')')
            self._generateParenthesis(left, right-1, result)
            result.pop()
        elif left == right:
            result.append('(')
            self._generateParenthesis(left-1, right, result)
            result.pop()
        else:
            result.append('(')
            self._generateParenthesis(left-1, right, result)
            result.pop()
            result.append(')')
            self._generateParenthesis(left, right-1, result)
            result.pop()

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self._generateParenthesis(n, n, [])
        return self.results


print(Solution().generateParenthesis(3))
