# /usr/bin/python
# coding: utf-8


class Solution(object):
    def __init__(self):
        self.results = []
        self.memo = {}
        self.length = 0

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        can_reach = [False for i in range(len(s)+1)]
        can_reach[0] = True
        for i in range(len(s)):
            self.memo[i] = []
            for word in wordDict:
                if s[i:].startswith(word):
                    self.memo[i].append(word)
                    can_reach[i+len(word)] |= can_reach[i]
        if not can_reach[-1]:
            return []
        self.length = len(s)
        self.work_break([], 0)
        return self.results

    def work_break(self, result, index):
        if index == self.length:
            self.results.append(' '.join(result))
        else:
            for word in self.memo[index]:
                result.append(word)
                self.work_break(result, index + len(word))
                result.pop()


print(Solution().wordBreak("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa", ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]))
print(Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]))
print(Solution().wordBreak("pineapplepenapple", ["apple", "pen", "applepen", "pine", "pineapple"]))
print(Solution().wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
