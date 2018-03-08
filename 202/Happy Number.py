# /usr/bin/python
# coding: utf-8


class Solution:
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        new_n = 0
        old_n = n
        history = set()
        while True:
            while old_n > 0:
                new_n += (old_n % 10) ** 2
                old_n //= 10
            if new_n == 1:
                return True
            else:
                if new_n in history:
                    return False
                else:
                    history.add(new_n)
                    old_n = new_n
                    new_n = 0


if __name__ == '__main__':
    assert Solution().isHappy(19) is True
