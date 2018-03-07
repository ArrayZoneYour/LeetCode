# /usr/bin/python
# coding: utf-8


class Solution:
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return list(nums1 & nums2)


if __name__ == '__main__':
    assert Solution().intersection([1, 2, 2, 1], [2, 2]) == [2]
