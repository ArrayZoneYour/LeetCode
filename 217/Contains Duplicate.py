# /usr/bin/python
# coding: utf-8


class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums) == 0:
            return False
        dic = {}  # 元素查找表
        for num in nums:
            if dic.__contains__(num):
                return True
            else:
                dic[num] = 1

        return False
