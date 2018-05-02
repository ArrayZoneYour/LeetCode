# /usr/bin/python
# coding: utf-8


class Solution:
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        level_1, level_2 = version1.split('.'), version2.split('.')
        length_1, length_2 = map(len, (level_1, level_2))
        for i in range(min(length_1, length_2)):
            if int(level_1[i]) > int(level_2[i]):
                return 1
            elif int(level_1[i]) < int(level_2[i]):
                return -1
        if length_1 > length_2:
            for num in level_1[min(length_1, length_2):]:
                if int(num) != 0:
                    return 1
            return 0
        elif length_1 < length_2:
            for num in level_2[min(length_1, length_2):]:
                if int(num) != 0:
                    return -1
            return 0
        else:
            return 0


assert Solution().compareVersion("19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.00.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000", "19.8.3.17.5.01.0.0.4.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0000.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.0.000000") == 0
assert Solution().compareVersion("0.1", "1.1") == -1
assert Solution().compareVersion("1", "2") == -1
assert Solution().compareVersion("1.0.1", "1") == 1
assert Solution().compareVersion("1", "1") == 0
assert Solution().compareVersion("1.0", "1") == 0
assert Solution().compareVersion("1.0.2.3", "1.0.2.3") == 0
assert Solution().compareVersion("7.5.2.4", "7.5.3") == -1
assert Solution().compareVersion("7.5.3.2", "7.5.2.5.6") == 1
