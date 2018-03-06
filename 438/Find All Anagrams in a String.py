# /usr/bin/python
# coding: utf-8


class Solution:
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counters = [0] * 123
        result = []
        # 收集p中所有元素(是否只出现一次？)
        for i in range(len(p)):
            counters[ord(p[i])] += 1
        # 不只出现一次，需要复制备份参考
        counters_run = [0] * 123
        pointer_l = 0
        pointer_r = 0
        score = 0
        # 搜寻Anagram
        while pointer_r < len(s):
            # 指针指向需要的元素
            # 指针指向了非法元素
            if not counters[ord(s[pointer_r])]:
                # 移动左侧指针直至指针重新回到同一起跑线
                while pointer_l != pointer_r:
                    counters_run[ord(s[pointer_l])] -= 1
                    pointer_l += 1
                    score -= 1
                # 两指针右移一位继续搜寻
                pointer_r += 1
                pointer_l += 1
            elif counters_run[ord(s[pointer_r])] < counters[ord(s[pointer_r])]:
                score += 1
                counters_run[ord(s[pointer_r])] += 1
                if score == len(p):
                    result.append(pointer_l)
                pointer_r += 1
            # 指针指向了重复元素
            else:
                # 移动左侧指针直至消除重复元素
                while counters_run[ord(s[pointer_r])] == counters[ord(s[pointer_r])]:
                    counters_run[ord(s[pointer_l])] -= 1
                    pointer_l += 1
                    score -= 1
        return result





if __name__ == '__main__':
    assert Solution().findAnagrams("cbaebabacd", "abc") == [0, 6]
    assert Solution().findAnagrams("abab", "ab") == [0, 1, 2]
