# /usr/bin/python
# coding: utf-8


class Solution:

    def __init__(self):
        self.results = []

    def _combinationSum(self, combination, candidates, sum, target):
        if sum == target:
            self.results.append(combination.copy())
        elif sum < target:
            for index, candidate in enumerate(candidates):
                if sum + candidate <= target:
                    combination.append(candidate)
                    self._combinationSum(combination, candidates[index:], sum + candidate, target)
                    combination.pop()

    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        for index, candidate in enumerate(candidates):
            if candidate <= target:
                self._combinationSum([candidate], candidates[index:], candidate, target)
        return self.results
