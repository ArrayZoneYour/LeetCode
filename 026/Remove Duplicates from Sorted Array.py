# /usr/bin/python
# coding: utf-8


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        curVal = 0
        cur = 0
        for i in range(len(nums)):
            if i == 0:  # 初始指针后移，读入第一个元素
                curVal = nums[0]
                cur += 1
                continue
            if curVal == nums[cur]:
                del nums[cur]
            else:
                curVal = nums[cur]
                cur += 1
        return cur


if __name__ == '__main__':
    nums = [1, 1, 2]
    assert Solution().removeDuplicates(nums) == 2
    assert nums == [1, 2]
