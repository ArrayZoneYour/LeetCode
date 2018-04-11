# /usr/bin/python
# coding: utf-8


class Solution:
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        RomanList = [
            ('', 'I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX'),
            ('', 'X', 'XX', 'XXX', 'XL', 'L', 'LX', 'LXX', 'LXXX', 'XC'),
            ('', 'C', 'CC', 'CCC', 'CD', 'D', 'DC', 'DCC', 'DCCC', 'CM'),
            ('', 'M', 'MM', 'MMM')
        ]
        result = []
        index = 0
        while num > 0:
            str_num = num % 10
            num //= 10
            result.append(RomanList[index][str_num])
            index += 1
        result.reverse()
        return ''.join(result)


print(Solution().intToRoman(12))
