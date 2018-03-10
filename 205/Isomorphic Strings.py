# /usr/bin/python
# coding: utf-8


class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        f = {}
        if len(s) != len(t):
            return False
        for _from, _to in zip(s, t):
            if _from in f:
                if f[_from] == _to:
                    continue
                else:
                    return False
            else:
                f[_from] = _to
        return len(set(f.values())) == len(f)


if __name__ == '__main__':
    assert Solution().isIsomorphic("egg", "add") is True
    assert Solution().isIsomorphic("foo", "bar") is False
    assert Solution().isIsomorphic("paper", "title") is True
    assert Solution().isIsomorphic("ppp", "tttt") is False
    assert Solution().isIsomorphic("pk", "tt") is False
