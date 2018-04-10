# /usr/bin/python
# coding: utf-8


class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # 循环len(nums)次，遇到等于val的元素执行del方法，否则指针加一
        cur = 0
        for i in range(len(nums)):
            if nums[cur] == val:
                del nums[cur]
            else:
                cur += 1
        return len(nums)


if __name__ == '__main__':
    test_nums = [3, 2, 2, 3]
    assert Solution().removeElement(test_nums, 2) == 2
    assert test_nums == [3, 3]
