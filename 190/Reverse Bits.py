# /usr/bin/python
# coding: utf-8


class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bit_list = []
        for i in range(32):
            if n == 0:
                bit_list.append(0)
            else:
                bit_list.append(n % 2)
                n //= 2
        size = 1
        result = 0
        for bit in bit_list[::-1]:
            if bit != 0:
                result += bit * size
            size *= 2
        return result


print(Solution().reverseBits(43261596))
