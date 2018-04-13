# /usr/bin/python
# coding: utf-8


class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return '1'
        result = '1'
        row = 1
        while row < n:
            cur = result[0]
            count = 1
            tmp = []
            for index in range(1, len(result)):
                if result[index] == cur:
                    count += 1
                else:
                    tmp.append(str(count))
                    tmp.append(str(cur))
                    cur = result[index]
                    count = 1
            tmp.append(str(count))
            tmp.append(str(cur))
            result = tmp
            row += 1
        return ''.join(result)


print(Solution().countAndSay(8))
