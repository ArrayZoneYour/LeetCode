# /usr/bin/python
# coding: utf-8


class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if not words or not s or len(s) < len(words) * len(words[0]):
            return []
        result = []
        word_length = len(words[0])
        decide_times = len(s) - len(words) * word_length + 1
        visited_init = {}
        for key in words:
            if key in visited_init:
                visited_init[key] += 1
            else:
                visited_init[key] = 1
        for i in range(decide_times):
            visited = visited_init.copy()
            stat_time = 0
            for j in range(len(words)):
                start_index = i+j*word_length
                word = s[start_index:start_index+word_length]
                if word in visited and visited[word]:
                    stat_time += 1
                    visited[word] -= 1
                else:
                    break
            if stat_time == len(words):
                result.append(i)
        return result


print(Solution().findSubstring("barfoothefoobarman", ["foo", "bar"]))
print(Solution().findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"]))
print(Solution().findSubstring("wordgoodgoodgoodbestword", ["word","good","best", "good"]))
