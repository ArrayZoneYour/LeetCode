# /usr/bin/python
# coding: utf-8


class Solution:
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        t = list(s)
        pointer_r = len(t) - 1
        pointer_l = 0
        while pointer_l < pointer_r:
            if t[pointer_l] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                if t[pointer_r] in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']:
                    t[pointer_l], t[pointer_r] = t[pointer_r], t[pointer_l]
                    pointer_l += 1
                    pointer_r -= 1
                else:
                    pointer_r -= 1
            else:
                pointer_l += 1
        return "".join(t)


if __name__ == '__main__':
    assert Solution().reverseVowels('hello') == 'holle'
    assert Solution().reverseVowels("leetcode") == "leotcede"
