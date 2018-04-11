# /usr/bin/python
# coding: utf-8


class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        RomanList = (
            {'': 0, 'I': 1, 'II': 2, 'III': 3, 'IV': 4, 'V': 5, 'VI': 6, 'VII': 7, 'VIII': 8, 'IX': 9},
            {'': 0, 'X': 1, 'XX': 2, 'XXX': 3, 'XL': 4, 'L': 5, 'LX': 6, 'LXX': 7, 'LXXX': 8, 'XC': 9},
            {'': 0, 'C': 1, 'CC': 2, 'CCC': 3, 'CD': 4, 'D': 5, 'DC': 6, 'DCC': 7, 'DCCC': 8, 'CM': 9},
            {'': 0, 'M': 1, 'MM': 2, 'MMM': 3}
        )
        result = 0
        index = 0
        factor = 1
        while s:
            if s[-4:] in RomanList[index]:
                result += RomanList[index][s[-4:]] * factor
                s = s[:-4]
            elif s[-3:] in RomanList[index]:
                result += RomanList[index][s[-3:]] * factor
                s = s[:-3]
            elif s[-2:] in RomanList[index]:
                result += RomanList[index][s[-2:]] * factor
                s = s[:-2]
            elif s[-1:] in RomanList[index]:
                result += RomanList[index][s[-1:]] * factor
                s = s[:-1]
            index += 1
            factor *= 10
        return result


print(Solution().romanToInt("MDCCCLXXXIV"))
