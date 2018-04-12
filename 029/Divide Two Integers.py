# /usr/bin/python
# coding: utf-8


class Solution:
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # 2147483647
        if dividend == 0 or abs(dividend) < abs(divisor):
            return 0
        if divisor == 0:
            return 2147483647
        flag = -1 if dividend < 0 < divisor or divisor < 0 < dividend else 1
        dividend, divisor = abs(dividend), abs(divisor)
        result_factor = [divisor]
        result = [1]
        while result_factor[-1] <= dividend:
            result_factor.append(result_factor[-1] * 2)
            result.append(result[-1] * 2)
        pointer = len(result) - 3
        while pointer >= 0:
            if result_factor[pointer] + result_factor[-2] <= dividend:
                result[-2] += result[pointer]
                result_factor[-2] += result_factor[pointer]
            pointer -= 1
        print(result, result_factor)
        if flag == 1:
            return min(result[-2], 2147483647)
        else:
            return -min(result[-2], 2147483648)


print(Solution().divide(2147483647, 3))
