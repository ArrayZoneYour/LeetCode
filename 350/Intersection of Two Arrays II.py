# /usr/bin/python
# coding: utf-8

from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = Counter(nums1)
        nums2 = Counter(nums2)
        counter = nums1 & nums2
        result_list = []
        for el in counter:
            result_list.extend([el] * counter[el])
        return result_list


if __name__ == '__main__':
    assert Solution().intersect([1, 2, 2, 1], [2, 2]) == [2, 2]
