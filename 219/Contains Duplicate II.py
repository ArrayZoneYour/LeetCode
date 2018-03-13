# /usr/bin/python
# coding: utf-8

class Solution:
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        dic = {}
        for index in range(len(nums)):
            if dic.__contains__(nums[index]):
                return True
            else:
                dic[nums[index]] = 1
            if len(dic) == k + 1:
                del dic[nums[index - k]]
        return False


print(Solution().containsNearbyDuplicate([1, 2, 1], 0) is False)
print(Solution().containsNearbyDuplicate([-1, -1], 1) is True)
