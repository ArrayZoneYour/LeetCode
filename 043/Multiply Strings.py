# /usr/bin/python
# coding: utf-8


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        result = 0
        nums1 = []
        nums2 = []
        factor = 1
        for el in num1[::-1]:
            nums1.append((ord(el) - 48) * factor)
            factor *= 10
        factor = 1
        for el in num2[::-1]:
            nums2.append((ord(el) - 48) * factor)
            factor *= 10
        for el_1 in nums1:
            for el_2 in nums2:
                result += el_1 * el_2
        return str(result)


print(Solution().multiply("123", "456"))
print(Solution().multiply("2", "3"))
print(Solution().multiply("12353536", "456654643"))
