# /usr/bin/python
# coding: utf-8


class Solution:

    def __init__(self):
        self.results = []

    def findCombination(self, arr, combination, sum, k, n):
        if sum == n and len(combination) == k:
            self.results.append(combination.copy())
        elif len(combination) < k:
            for index, i in enumerate(arr):
                if sum + i <= n:
                    combination.append(i)
                    self.findCombination(arr[index+1:], combination, sum + i, k, n)
                    combination.pop()

    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for i in arr:
            if i <= n:
                self.findCombination(arr[i:], [i], i, k, n)
        return self.results
