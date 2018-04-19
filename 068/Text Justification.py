# /usr/bin/python
# coding: utf-8


class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        results = [[]]
        curr_width = 0
        index = 0
        for word in words:
            if curr_width + len(word) + len(results[index]) > maxWidth:
                if len(results[index]) == 1:
                    results[index] = results[index][0] + ' ' * (maxWidth - len(results[index][0]))
                else:
                    while curr_width < maxWidth:
                        for i in range(len(results[index])-1):
                            results[index][i] += ' '
                            curr_width += 1
                            if curr_width == maxWidth:
                                break
                    results[index] = ''.join(results[index])
                index += 1
                results.append([])
                curr_width = 0
            results[index].append(word)
            curr_width += len(word)
        if len(results[index]) == 1:
            results[index] = results[index][0] + ' ' * (maxWidth - len(results[index][0]))
        else:
            curr_width += len(results[index]) - 1
            while curr_width < maxWidth:
                results[index][-1] += ' '
                curr_width += 1
            results[index] = ' '.join(results[index])
        return results


print(Solution().fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16))
print(Solution().fullJustify(["What","must","be","acknowledgment","shall","be"], 16))
print(Solution().fullJustify(["Science","is","what","we","understand","well","enough","to","explain",
                              "to","a","computer.","Art","is","everything","else","we","do"], 20))
print(Solution().fullJustify(["What","must","be","shall","be."], 12))
