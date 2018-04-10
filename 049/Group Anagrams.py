# /usr/bin/python
# coding: utf-8


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dic = {}
        for str in strs:
            ordered_str = ''.join(sorted(str))
            if dic.__contains__(ordered_str):
                dic[ordered_str].append(str)
            else:
                dic[ordered_str] = [str]
        return list(dic.values())


print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
