# /usr/bin/python
# coding: utf-8


class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        height_stack, pos_stack = [], []
        max_size = 0
        for index in range(len(heights)):
            if len(height_stack) == 0 or heights[index] > height_stack[-1]:
                height_stack.append(heights[index])
                pos_stack.append(index)
            elif heights[index] < height_stack[-1]:
                while len(height_stack) and heights[index] < height_stack[-1]:
                    pos_left = pos_stack.pop()
                    height_left = height_stack.pop()
                    tmp_size = (index - pos_left) * height_left
                    max_size = max(max_size, tmp_size)
                height_stack.append(heights[index])
                pos_stack.append(pos_left)
        while len(height_stack):
            pos_left = pos_stack.pop()
            height_left = height_stack.pop()
            tmp_size = (len(heights) - pos_left) * height_left
            max_size = max(max_size, tmp_size)
        return max_size


print(Solution().largestRectangleArea([2, 1, 2]))
print(Solution().largestRectangleArea([2,1,5,6,2,3]))
print(Solution().largestRectangleArea([2]))
