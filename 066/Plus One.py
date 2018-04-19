# /usr/bin/python
# coding: utf-8


class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        full = 0
        digits[-1] += 1
        for i in range(1, len(digits)+1):
            digits[-i] += full
            if digits[-i] == 10:
                digits[-i] = 0
                full = 1
            else:
                full = 0
            if not full:
                break
        if digits[0] == 10 or full:
            digits[0] = 0
            digits.insert(0, 1)
        return digits


print(Solution().plusOne([9, 9, 9]))
print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9]))
