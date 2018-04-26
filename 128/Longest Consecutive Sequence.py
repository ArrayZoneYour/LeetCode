# /usr/bin/python
# coding: utf-8


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        longest = 0
        num_dic = {}
        for num in nums:
            if num not in num_dic:
                if num-1 in num_dic and num+1 in num_dic:
                    left = num_dic[num-1][0]
                    right = num_dic[num+1][1]
                    num_dic[left][1] = right
                    num_dic[right][0] = left
                    num_dic[num] = [left, right]
                    longest = max(longest, right - left + 1)
                elif num-1 in num_dic:
                    left = num_dic[num-1][0]
                    num_dic[left][1] = num
                    num_dic[num] = [left, num]
                    longest = max(longest, num - left + 1)
                elif num+1 in num_dic:
                    right = num_dic[num+1][1]
                    num_dic[right][0] = num
                    num_dic[num] = [num, right]
                    longest = max(longest, right - num + 1)
                else:
                    num_dic[num] = [num, num]
                    longest = max(1, longest)
        return longest


print(Solution().longestConsecutive([-1,9,-3,-6,7,-8,-6,2,9,2,3,-2,4,-1,0,6,1,-9,6,8,6,5,2]))
print(Solution().longestConsecutive([1, 2, 0, 1]))
print(Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
