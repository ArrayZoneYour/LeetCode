# /usr/bin/python
# coding: utf-8


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        match_board = [[False for i in range(len(s)+1)] for j in range(len(p)+1)]
        match_board[0][0] = True
        start_col = 0
        for row in range(1, len(p)+1):
            if p[row-1] == '*':
                tmp = start_col
                while tmp <= len(s):
                    match_board[row][tmp] = True
                    tmp += 1
            elif p[row-1] == '?':
                tmp = start_col + 1
                start_col += 1
                while tmp <= len(s):
                    if match_board[row-1][tmp-1]:
                        match_board[row][tmp] = True
                    tmp += 1
            else:
                tmp = start_col + 1
                first_col = False
                while tmp <= len(s):
                    if match_board[row - 1][tmp - 1] and s[tmp-1] == p[row-1]:
                        if not first_col:
                            first_col = True
                            start_col = tmp
                        match_board[row][tmp] = True
                    tmp += 1
                if not first_col:
                    return False
        return match_board[-1][-1]


# TODO There has a better alg to use
print(Solution().isMatch("mississippi", "m??*ss*?i*pi"))
print(Solution().isMatch("aab", "c*a*b"))
print(Solution().isMatch("acdcb", "a*c?b"))
print(Solution().isMatch("adceb", "*a*b"))
print(Solution().isMatch("cb", "?a"))
print(Solution().isMatch("aa", "*"))
print(Solution().isMatch("aa", "a"))
