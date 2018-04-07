# /usr/bin/python
# coding: utf-8
import time


class Solution:

    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int[1, 1, 1, 1, 1]
        :rtype: int
        """
        if S > 1000:
            return 0
        mem_pre = [0] * 2001
        pre = set()
        mem_pre[nums[0]] += 1
        mem_pre[-nums[0]] += 1
        pre.add(nums[0])
        pre.add(-nums[0])
        for num in nums[1:]:
            mem_cur = [0] * 2001
            curr = set()
            while pre:
                el = pre.pop()
                mem_cur[el+num] += mem_pre[el]
                curr.add(el+num)
                mem_cur[el-num] += mem_pre[el]
                curr.add(el-num)
            pre = curr
            mem_pre = mem_cur
        return mem_pre[S]


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
start = time.time()
print(Solution().findTargetSumWays([27,22,39,22,40,32,44,45,46,8,8,21,27,8,11,29,16,15,41,0], 10))
print(Solution().findTargetSumWays([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 10))
end = time.time()
print(str(end - start))
