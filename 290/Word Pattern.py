# /usr/bin/python
# coding: utf-8


class Solution:
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        # 定义映射
        f = {}
        if len(pattern) != len(str.split(' ')):
            return False
        for _from, _to in zip(pattern, str.split(' ')):
            if _from in f:
                if f[_from] == _to:
                    continue
                else:
                    return False
            else:
                f[_from] = _to
        return len(set(f.values())) == len(f)



if __name__ == '__main__':
    assert Solution().wordPattern("abba", "dog cat cat dog") is True
    assert Solution().wordPattern("abba", "dog cat cat fish") is False
    assert Solution().wordPattern("aaaa", "dog cat cat dog") is False
    assert Solution().wordPattern("abba", "dog dog dog dog") is False
