# /usr/bin/python
# coding: utf-8


class Solution:
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        while len(height) < 3:
            return 0
        pointer_l = 0
        while pointer_l < len(height) - 1 and height[pointer_l + 1] >= height[pointer_l]:
            pointer_l += 1
        if pointer_l == len(height) - 1:
            return 0
        result = 0
        while pointer_l < len(height) - 1:
            temp_r = pointer_l + 1
            pointer_r = pointer_l + 1
            while temp_r < len(height):
                if height[temp_r] >= height[pointer_r]:
                    pointer_r = temp_r
                if height[temp_r] > height[pointer_l]:
                    break
                temp_r += 1
            for el in height[pointer_l+1:pointer_r+1]:
                if pointer_r < len(height) - 1 and height[pointer_r+1] >= height[pointer_r]:
                    v = min(height[pointer_l], height[pointer_r+1]) - el
                    if v > 0:
                        result += v
                else:
                    v = min(height[pointer_l], height[pointer_r]) - el
                    if v > 0:
                        result += v
            pointer_l = pointer_r
        return result


print(Solution().trap([4,2,0,3,2,5]))  # 9
print(Solution().trap([5,4,1,2]))  # 1
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))  # 6
print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,3]))  # 9
print(Solution().trap([0,2,0]))  # 0
print(Solution().trap([5,2,1,2,1,5]))  # 14
