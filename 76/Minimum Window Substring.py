# /usr/bin/python
# coding: utf-8


class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # 收集需要被包含的元素
        counter = [0] * 123
        result = ""
        # 收集p中所有元素(是否只出现一次？)
        for i in range(len(t)):
            counter[ord(t[i])] += 1
        # 不只出现一次，需要复制备份参考
        counter_run = [0] * 123
        pointer_l = 0
        pointer_r = 0
        score_max = len(t)
        score = 0
        while pointer_r < len(s):
            if counter_run[ord(s[pointer_r])] < counter[ord(s[pointer_r])]:
                score += 1
                counter_run[ord(s[pointer_r])] += 1
                # 判断两指针间是否为可行解
                while score == score_max:
                    # 判断左移的元素是否需要计数
                    if counter[ord(s[pointer_l])]:
                        if counter_run[ord(s[pointer_l])] <= counter[ord(s[pointer_l])]:
                            # 判断当前解是否为最优解
                            if result == "" or pointer_r - pointer_l + 1 < len(result):
                                result = s[pointer_l:pointer_r+1]
                            score -= 1
                        counter_run[ord(s[pointer_l])] -= 1
                    pointer_l += 1
                pointer_r += 1
            else:
                counter_run[ord(s[pointer_r])] += 1
                pointer_r += 1
        return result


if __name__ == '__main__':
    assert Solution().minWindow("ADOBECODEBANC", "ABC") == "BANC"
