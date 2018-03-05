# /usr/bin/python
# coding: utf-8


class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        pointer_l = 0
        pointer_r = len(s) - 1
        while pointer_l < pointer_r:
            if 'a' <= s[pointer_l] <= 'z':
                if 'a' <= s[pointer_r] <= 'z':
                    if s[pointer_l] != s[pointer_r]:
                        return False
                    pointer_l += 1
                    pointer_r -= 1
                elif 'A' <= s[pointer_r] <= 'Z':
                    if s[pointer_r].lower() != s[pointer_l]:
                        return False
                    pointer_l += 1
                    pointer_r -= 1
                elif '0' <= s[pointer_r] <= '9':
                    return False
                else:
                    pointer_r -= 1
            elif 'A' <= s[pointer_l] <= 'Z':
                if 'a' <= s[pointer_r] <= 'z':
                    if s[pointer_l] != s[pointer_r].upper():
                        return False
                    pointer_l += 1
                    pointer_r -= 1
                elif 'A' <= s[pointer_r] <= 'Z':
                    if s[pointer_r] != s[pointer_l]:
                        return False
                    pointer_l += 1
                    pointer_r -= 1
                elif '0' <= s[pointer_r] <= '9':
                    return False
                else:
                    pointer_r -= 1
            elif '0' <= s[pointer_l] <= '9':
                if 'a' <= s[pointer_r] <= 'z' or 'A' <= s[pointer_r] <= 'Z' or '0' <= s[pointer_r] <= '9':
                    if s[pointer_r] != s[pointer_l]:
                        return False
                    pointer_l += 1
                    pointer_r -= 1
                else:
                    pointer_r -= 1
            else:
                pointer_l += 1
        return True


if __name__ == '__main__':
    test_str = "A man, a plan, a canal: Panama"
    assert Solution().isPalindrome("0P") is False
    assert Solution().isPalindrome(test_str) is True
    assert Solution().isPalindrome("race a car") is False
