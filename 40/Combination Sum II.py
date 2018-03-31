# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.results = []

    def combine(self, combination, candidates, sum, target):
        if sum == target:
            self.results.append(combination.copy())
        else:
            last_value = None
            for index, candidate in enumerate(candidates):
                if last_value != candidate:
                    if sum + candidate < target:
                        combination.append(candidate)
                        self.combine(combination, candidates[index+1:], sum + candidate, target)
                        last_value = candidate
                        combination.pop()
                    if sum + candidate == target:
                        self.results.append(combination.copy())

    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        last_value = None
        for index, candidate in enumerate(candidates):
            if last_value != candidate and candidate <= target:
                self.combine([candidate], candidates[index+1:], candidate, target)
                last_value = candidate
        return self.results
