# /usr/bin/python
# coding: utf-8


class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:  # 处理空数组
            return 0
        curVal = nums[0]  # 当前值
        curCount = 1  # 当前计数
        cur = 1  # 当前指针
        for i in range(0, len(nums)-1):
            if nums[cur] == curVal:
                if curCount == 2:  # 计数等于两个，执行删除操作
                    del nums[cur]
                else:
                    curCount += 1
                    cur += 1
            else: # 更新值和指针
                curVal = nums[cur]
                curCount = 1
                cur += 1
        return len(nums)


if __name__ == '__main__':
    nums = [1, 1, 1, 2, 2, 3]
    assert Solution().removeDuplicates(nums) == 5
    assert nums == [1, 1, 2, 2, 3]
    nums = [0, 0, 0, 0, 0]
    assert Solution().removeDuplicates(nums) == 2
    assert nums == [0, 0]
