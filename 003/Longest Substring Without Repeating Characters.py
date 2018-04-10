# /usr/bin/python
# coding: utf-8


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        counter = [0] * 127
        pointer_l = 0
        pointer_r = 0
        result = 0
        while pointer_r < len(s):
            if counter[ord(s[pointer_r])] == 0:
                counter[ord(s[pointer_r])] = 1
                pointer_r += 1
                if pointer_r - pointer_l > result:
                    result = pointer_r - pointer_l
            else:
                counter[ord(s[pointer_l])] = 0
                pointer_l += 1
        return result


if __name__ == '__main__':
    assert Solution().lengthOfLongestSubstring("abcabcbb") == 3
    assert Solution().lengthOfLongestSubstring("bbbbb") == 1
    assert Solution().lengthOfLongestSubstring("pwwkew") == 3
