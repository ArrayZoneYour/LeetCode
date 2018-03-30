# /usr/bin/python
# coding: utf-8


class Solution:

    def _permute(self, nums, visited, result, results):
        if len(result) == len(nums):
            results.append(result.copy())
        else:
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    result.append(nums[i])
                    self._permute(nums, visited, result, results)
                    result.pop()
                    visited[i] = False

    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        results = []
        visited = [False] * len(nums)
        for i in range(len(nums)):
            visited[i] = True
            self._permute(nums, visited, [nums[i]], results)
            visited[i] = False
        return results
