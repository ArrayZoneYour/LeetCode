# /usr/bin/python
# coding: utf-8


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        record = {}
        for i, el in enumerate(nums):
            if target - el in record:
                return [record[target - el], i]
            else:
                record[el] = i


if __name__ == '__main__':
    assert Solution().twoSum([2, 7, 11, 15], 9) == [0, 1]
