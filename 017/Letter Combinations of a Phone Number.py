# /usr/bin/python
# coding: utf-8


class Solution(object):
    def __init__(self):
        self.keyboard = [' ', None, 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']

    def getCombination(self, exist_s, digits, result):
        if not digits:
            result.append(exist_s)
        else:
            for el in self.keyboard[int(digits[0])]:
                self.getCombination(exist_s + el, digits[1:], result)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        result = []
        if not digits:
            return result
        self.getCombination('', digits, result)
        return result
