# /usr/bin/python
# coding: utf-8


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result = []
        full = 0
        add_times = min(len(a), len(b))
        for i in range(add_times):
            one_add_result = int(a[-i - 1]) + int(b[-i - 1]) + full
            if one_add_result == 1:
                result.append('1')
                full = 0
            elif one_add_result == 2:
                result.append('0')
                full = 1
            elif one_add_result == 0:
                result.append('0')
                full = 0
            elif one_add_result == 3:
                result.append('1')
                full = 1
        if len(a) > len(b):
            for i in range(len(a) - len(b)):
                one_add_result = int(a[-add_times-i-1]) + full
                if one_add_result == 1:
                    result.append('1')
                    full = 0
                elif one_add_result == 2:
                    result.append('0')
                    full = 1
                elif one_add_result == 0:
                    result.append('0')
                    full = 0
        elif len(a) < len(b):
            for i in range(len(b) - len(a)):
                one_add_result = int(b[-add_times-i-1]) + full
                if one_add_result == 1:
                    result.append('1')
                    full = 0
                elif one_add_result == 2:
                    result.append('0')
                    full = 1
                elif one_add_result == 0:
                    result.append('0')
                    full = 0
        if full == 1:
            result.append('1')
        result.reverse()
        return ''.join(result)


print(Solution().addBinary('1', '11111'))
