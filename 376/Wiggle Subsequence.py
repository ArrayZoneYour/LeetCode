# /usr/bin/python
# coding: utf-8


class Solution:
    def __init__(self):
        self.UpperStartLen = 1
        self.DownStartLen = 1

    def findIncreaseElement(self, last, nums, UpperStart):
        for index, num in enumerate(nums):
            if num > last:
                if UpperStart:
                    self.UpperStartLen += 1
                else:
                    self.DownStartLen += 1
                self.findDecreaseElement(num, nums[index+1:], UpperStart)
                break
            else:
                last = num

    def findDecreaseElement(self, last, nums, UpperStart):
        for index, num in enumerate(nums):
            if num < last:
                if UpperStart:
                    self.UpperStartLen += 1
                else:
                    self.DownStartLen += 1
                self.findIncreaseElement(num, nums[index+1:], UpperStart)
                break
            else:
                last = num

    def wiggleMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0
        cmp_num = nums[0]
        index = 0
        while index < len(nums) and nums[index] == cmp_num:
            index += 1
        if index == len(nums):
            return 1
        if nums[index] > nums[0]:
            self.findIncreaseElement(nums[0], nums[1:], True)
            return self.UpperStartLen
        elif nums[index] < nums[0]:
            self.findDecreaseElement(nums[0], nums[1:], False)
            return self.DownStartLen


assert Solution().wiggleMaxLength([1]) == 1
assert Solution().wiggleMaxLength([1,1,1,1,7,4,9,2,5]) == 6
assert Solution().wiggleMaxLength([1,7,4,9,2,5]) == 6
assert Solution().wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]) == 7
assert Solution().wiggleMaxLength([1,2,3,4,5,6,7,8,9]) == 2
