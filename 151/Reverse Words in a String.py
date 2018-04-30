# /usr/bin/python
# coding: utf-8


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        str_list = s.split(' ')
        str_list = [el for el in str_list if el]
        str_list.reverse()
        return ' '.join(str_list)


print(Solution().reverseWords(" the   sky is blue  "))
