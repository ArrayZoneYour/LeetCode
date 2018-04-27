# /usr/bin/python
# coding: utf-8


class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return -1
        gas_v = 0
        start_index = 0
        index = 0
        for c, g in zip(cost, gas):
            if gas_v - c + g < 0:
                gas_v = 0
                index += 1
                start_index = index
            else:
                gas_v += g - c
                index += 1
        return start_index


print(Solution().canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]))
print(Solution().canCompleteCircuit([2,3,4], [3,4,3]))
