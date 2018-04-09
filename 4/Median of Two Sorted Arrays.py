# /usr/bin/python
# coding: utf-8
import math


class Solution:

    def getCutArrays(self, nums1, nums2, left_num):
        if not left_num:
            return nums1, nums2
        remove_num = math.ceil(left_num/2)
        if len(nums1) < remove_num:
            return self.getCutArrays(nums1, nums2[remove_num:], left_num - remove_num)
        if len(nums2) < remove_num:
            return self.getCutArrays(nums1[remove_num:], nums2, left_num - remove_num)
        if nums1[remove_num-1] < nums2[remove_num-1]:
            return self.getCutArrays(nums1[remove_num:], nums2, left_num - remove_num)
        else:
            return self.getCutArrays(nums1, nums2[remove_num:], left_num - remove_num)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)
        nums1, nums2 = self.getCutArrays(nums1, nums2, (m+n-1) // 2)
        if (m + n) % 2:
            return float(min(nums1[:1] + nums2[:1]))
        else:
            results = sorted(nums1[:2] + nums2[:2])
            result = (results[0] + results[1]) / 2.0
            return result


print(Solution().findMedianSortedArrays([1, 3], [2]))
print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5, 6, 7]))
