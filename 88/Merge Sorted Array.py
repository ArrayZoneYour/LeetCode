# /usr/bin/python
# coding: utf-8


class Solution:
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        point_1 = m - 1
        point_2 = n - 1
        point = m + n - 1
        nums1.extend(nums2[:m+n-len(nums1)])
        while point_1 > -1 and point_2 > -1:
            if nums1[point_1] < nums2[point_2]:
                nums1[point] = nums2[point_2]
                point -= 1
                point_2 -= 1
            else:
                nums1[point] = nums1[point_1]
                point -= 1
                point_1 -= 1
        if point_2 == -1:
            pass
        else:
            nums1[:point_2 + 1] = nums2[:point_2 + 1]



if __name__ == '__main__':
    nums1 = [0, 1, 2]
    nums2 = [1, 7, 9, 11]
    Solution().merge(nums1, 3, nums2, 4)
    assert nums1 == [0, 1, 1, 2, 7, 9, 11]
    nums1 = [0]
    nums2 = [1]
    Solution().merge(nums1, 0, nums2, 1)
    assert nums1 == [1]
