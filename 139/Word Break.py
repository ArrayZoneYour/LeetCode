# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.success = False
        self.visited = []

    def _wordBreak(self, s, wordDict, index):
        if self.success:
            return
        for word in wordDict:
            if s[index:].startswith(word):
                if s[index:] == word:
                    self.success = True
                elif not self.visited[index+len(word)]:
                    self._wordBreak(s, wordDict, index+len(word))
                    self.visited[index+len(word)] = True

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: bool
        """
        self.visited = [False] * (len(s) + 1)
        self._wordBreak(s, wordDict, 0)
        return self.success


print(Solution().wordBreak("bb", ["a", "b", "bbb", "bbbb"]))
print(Solution().wordBreak("leetcode", ["leet", "code"]))
print(Solution().wordBreak("ccaccc", ["cc", "ac"]))
print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab"
,["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
