# /usr/bin/python
# coding: utf-8


class Solution:
    def findCombination(self, combination, n, k, results, index):
        if len(combination) == k:
            results.append(combination.copy())
        else:
            for i in range(index + 1, n+1):
                if n - index >= k - len(combination):
                    combination.append(i)
                    self.findCombination(combination, n, k, results, i)
                    combination.pop()

    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        if k > n:
            return []
        if k == 1:
            return [[i] for i in range(1, n+1)]
        if k == n:
            return [list(range(1, n+1))]
        results = []
        for i in range(1, n+1):
            if n - i + 1 >= k:
                self.findCombination([i], n, k, results, i)
        return results

