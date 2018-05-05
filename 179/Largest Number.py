# /usr/bin/python
# coding: utf-8


class Solution:
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        nums = [str(num) for num in nums]
        result = self.qsort(nums)
        result = ''.join(result)
        result = result.lstrip('0')
        if not result:
            return '0'
        return result

    def qsort(self, nums):
        if not nums:
            return []
        left, medium, right = [], [], []
        pivot = nums[len(nums) // 2]
        for num in nums:
            flag = self.big_judge(num, pivot)
            if flag == 0:
                medium.append(num)
            elif flag == -1:
                right.append(num)
            else:
                left.append(num)
        if len(left) <= 1 and len(right) <= 1:
            return left + medium + right
        else:
            return self.qsort(left) + medium + self.qsort(right)

    def big_judge(self, num1, num2):
        if num1 == num2:
            return 0
        if len(num1) == len(num2):
            if num1 > num2:
                return 1
            elif num1 == num2:
                return 0
            else:
                return -1
        if num1 > num2:
            if num1.startswith(num2):
                return self.big_judge(num1[len(num2):], num2)
            else:
                return 1
        else:
            if num2.startswith(num1):
                return self.big_judge(num1, num2[len(num1):])
            else:
                return -1


print(Solution().largestNumber([3, 30, 34, 5, 9]))
print(Solution().largestNumber([10, 2]))
print(Solution().largestNumber([34, 343, 3433, 344, 3435]))
print(Solution().largestNumber([0, 0]))
print(Solution().largestNumber([0, 2, 20]))
