# /usr/bin/python
# coding: utf-8


class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        current_result = []
        nums.sort()
        n = len(nums)
        for i in range(n-3):
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, n-2):
                if nums[j] + nums[j+1] + nums[j+2] > target - nums[i]:
                    break
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue
                pointer_left = j+1
                pointer_right = n-1
                sum_two = target - nums[i] - nums[j]
                while pointer_left < pointer_right:
                    if nums[pointer_left] + nums[pointer_right] == sum_two:
                        if current_result != [nums[i], nums[j], nums[pointer_left], nums[pointer_right]]:
                            result.append([nums[i], nums[j], nums[pointer_left], nums[pointer_right]])
                            current_result = [nums[i], nums[j], nums[pointer_left], nums[pointer_right]]
                        pointer_left += 1
                        pointer_right -= 1
                    elif nums[pointer_left] + nums[pointer_right] < sum_two:
                        pointer_left += 1
                    else:
                        pointer_right -= 1
        return result


if __name__ == '__main__':
    assert Solution().fourSum([0, 0, 0, 0], 0) == [[0, 0, 0, 0]]
    assert Solution().fourSum([1, 0, -1, 0, -2, 2], 0) == [
        [-2, -1, 1, 2],
        [-2, 0, 0, 2],
        [-1, 0, 0, 1]
    ]
