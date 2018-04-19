# /usr/bin/python
# coding: utf-8


class Solution:
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.strip(' ')
        s = s.lstrip('+')
        if 'e' in s:
            s = s.split('e')
            if len(s) == 2:
                if s[0] and s[0][0] == '-':
                    if s[1] and (s[1][0] == '+' or s[1][0] == '-'):
                        return s[0][1:].replace('.', '', 1).isnumeric() and s[1][1:].isnumeric()
                    return s[0][1:].replace('.', '', 1).isnumeric() and s[1].isnumeric()
                if s[1] and (s[1][0] == '+' or s[1][0] == '-'):
                    return s[0].replace('.', '', 1).isnumeric() and s[1][1:].isnumeric()
                return s[0].replace('.', '', 1).isnumeric() and s[1].isnumeric()
            else:
                return False
        if '.' in s:
            s = s.split('.')
            if len(s) == 2:
                if s[0] and s[0][0] == '-':
                    return (not s[0][1:] or s[0][1:].isnumeric()) and (not s[1] or s[1].isnumeric()) and \
                           (s[0][1:].isnumeric() or s[1].isnumeric())
                return (not s[0] or s[0].isnumeric()) and (not s[1] or s[1].isnumeric()) and \
                       (s[0].isnumeric() or s[1].isnumeric())
            else:
                return False
        if len(s) > 1 and s[0] == '-':
            return s[1:].isnumeric()
        else:
            return s.isnumeric()


print(Solution().isNumber("32.e-80123"))
print(Solution().isNumber("459277e38+"))  # False
print(Solution().isNumber("- e"))  # False
print(Solution().isNumber("ee"))  # False
print(Solution().isNumber("e"))   # False
print(Solution().isNumber(" 005047e+6"))
print(Solution().isNumber("-3.e6"))
print(Solution().isNumber("46.e3"))
print(Solution().isNumber(" 1"))
print(Solution().isNumber("+ 1"))  # False
print(Solution().isNumber("+.1"))
print(Solution().isNumber("-01"))
print(Solution().isNumber("-1."))
print(Solution().isNumber("3."))
print(Solution().isNumber("2e10"))
print(Solution().isNumber("0"))
print(Solution().isNumber("0.1"))
print(Solution().isNumber("abc"))
print(Solution().isNumber("1 a"))
print(Solution().isNumber("1 "))
print(Solution().isNumber(".1 "))
print(Solution().isNumber(".."))
print(Solution().isNumber("."))

