# /usr/bin/python
# coding: utf-8


class Solution:
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        flag = '' if (numerator >= 0 and denominator > 0) or (numerator <= 0 and denominator < 0) else '-'
        numerator, denominator = abs(numerator), abs(denominator)
        int_part = numerator // denominator
        dem_part = numerator % denominator
        if dem_part == 0:
            return flag + str(int_part)
        else:
            result = ''
            int_part = str(int_part)
            memo = {dem_part: 0}
            index = 0
            while dem_part:
                dem_part *= 10
                result += str(dem_part // denominator)
                if dem_part % denominator in memo:
                    return flag + int_part + '.' + result[:memo[dem_part % denominator]] + \
                           '(' + result[memo[dem_part % denominator]:] + ')'
                index += 1
                memo[dem_part % denominator] = index
                dem_part %= denominator
            return flag + int_part + '.' + result


print(Solution().fractionToDecimal(-2147483648, 1))
print(Solution().fractionToDecimal(1, 6))
print(Solution().fractionToDecimal(1, 2))
print(Solution().fractionToDecimal(2, 1))
print(Solution().fractionToDecimal(2, 3))
print(Solution().fractionToDecimal(2, 7))
print(Solution().fractionToDecimal(9, 7))
print(Solution().fractionToDecimal(1, 17))
print(Solution().fractionToDecimal(1, 12))
print(Solution().fractionToDecimal(-50, 8))
print(Solution().fractionToDecimal(0, 3))
