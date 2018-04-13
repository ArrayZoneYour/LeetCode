# /usr/bin/python
# coding: utf-8


class Solution(object):
    def longestValidParentheses(self, s):
        # dp solution
        dp = [0] * len(s)
        result = leftCount = 0
        for i in range(len(s)):
            if s[i] == '(':
                leftCount += 1
            elif leftCount > 0:
                dp[i] = dp[i - 1] + 2
                dp[i] += (dp[i - dp[i]] if i >= dp[i] else 0)
                result = max(result, dp[i])
                leftCount -= 1
        return result


# TODO: 这个问题后面需要复习
print(Solution().longestValidParentheses("(()(((()"))
print(Solution().longestValidParentheses("()(()"))  # 2
print(Solution().longestValidParentheses(")()())"))  # 4
print(Solution().longestValidParentheses("(()"))  # 2
print(Solution().longestValidParentheses("())()"))  # 2
print(Solution().longestValidParentheses("(()()"))  # 4
print(Solution().longestValidParentheses("()()"))  # 4
