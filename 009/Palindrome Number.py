# /usr/bin/python
# coding: utf-8


class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        if x < 10:
            return True
        floor = 10
        ceil = 10
        while ceil * 10 <= x:
            ceil *= 10
        while ceil >= floor:
            if x % floor // (floor // 10) != x // ceil % 10:
                return False
            else:
                ceil /= 10
                floor *= 10
        return True


print(Solution().isPalindrome(11))
print(Solution().isPalindrome(100))
print(Solution().isPalindrome(1133))
print(Solution().isPalindrome(3113))
print(Solution().isPalindrome(-3113))
