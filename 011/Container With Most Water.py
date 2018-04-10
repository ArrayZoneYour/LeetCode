# /usr/bin/python
# coding: utf-8


class Solution:
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        pointer_l = 0
        pointer_r = len(height) - 1
        h_water = min(height[pointer_l], height[pointer_r])  # 可以达到的水位高度
        V_water = 0
        while pointer_r > pointer_l:
            if height[pointer_r] < height[pointer_l]:
                if height[pointer_r] * (pointer_r - pointer_l) > V_water:
                    V_water = height[pointer_r] * (pointer_r - pointer_l)
                pointer_r -= 1
            else:
                if height[pointer_l] * (pointer_r - pointer_l) > V_water:
                    V_water = height[pointer_l] * (pointer_r - pointer_l)
                pointer_l += 1
        return V_water


if __name__ == '__main__':
    pass
