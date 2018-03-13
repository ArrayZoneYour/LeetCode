# /usr/bin/python
# coding: utf-8


class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        counter_l = {}
        counter_r = {}
        result = 0
        for el_A in A:
            for el_B in B:
                _sum = el_A + el_B
                if counter_l.__contains__(_sum):
                    counter_l[_sum] += 1
                else:
                    counter_l[_sum] = 1

        for el_C in C:
            for el_D in D:
                _sum = el_C + el_D
                if counter_r.__contains__(_sum):
                    counter_r[_sum] += 1
                else:
                    counter_r[_sum] = 1

        for el in counter_l:
            if -el in counter_r:
                result += counter_l[el] * counter_r[-el]

        return result


print(Solution().fourSumCount([1, 2], [-2, -1], [-1, 2], [0, 2]) == 2)
