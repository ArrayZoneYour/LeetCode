# /usr/bin/python
# coding: utf-8


class Solution:

    def IsContinous(self, nums):
        nums = [num for num in nums if num != 0]
        num_table = {nums[0]}
        minimum = maximum = nums[0]
        for num in nums[1:]:
            if num in num_table:
                return False
            else:
                maximum = max(maximum, num)
                minimum = min(minimum, num)
                if maximum - minimum > 4:
                    return False
                num_table.add(num)
        return True


assert Solution().IsContinous([0, 2, 5, 4, 0]) is True
assert Solution().IsContinous([0, 1, 3, 4, 0]) is True
assert Solution().IsContinous([0, 2, 3, 7, 0]) is False
assert Solution().IsContinous([5, 2, 3, 4, 1]) is True
assert Solution().IsContinous([5, 2, 3, 4, 11]) is False
assert Solution().IsContinous([0, 5, 1, 3, 4]) is True
assert Solution().IsContinous([0, 0, 1, 0, 0]) is True
assert Solution().IsContinous([2, 3, 0, 0, 6]) is True
