# /usr/bin/python
# coding: utf-8


class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return 0
        max_sequence = s[0]
        for middle_pointer in range(1, len(s)-1):
            pointer_l = pointer_r = middle_pointer
            while pointer_l > 0 and pointer_r < len(s)-1 and s[pointer_l-1] == s[pointer_r+1]:
                pointer_l -= 1
                pointer_r += 1
            if pointer_r - pointer_l + 1 > len(max_sequence):
                max_sequence = s[pointer_l:pointer_r+1]
        for pointer_l, pointer_r in zip(range(0, len(s)-1), range(1, len(s))):
            if s[pointer_l] == s[pointer_r]:
                while pointer_l > 0 and pointer_r < len(s)-1 and s[pointer_l - 1] == s[pointer_r + 1]:
                    pointer_l -= 1
                    pointer_r += 1
                if pointer_r - pointer_l + 1 > len(max_sequence):
                    max_sequence = s[pointer_l:pointer_r + 1]
        return max_sequence


print(Solution().longestPalindrome("b" * 499 + "q" * 500))
