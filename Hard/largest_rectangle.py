class Solution:
    def largestRectangleArea(self, heights):
        max_area = 0
        stack = []
        n = len(heights)

        for i in range(n + 1):
            curr_height = 0 if i == n else heights[i]
            while stack and curr_height < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
        while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
        right[i] = stack[-1] if stack else n
        stack.append(i)

        max_area = 0
        for i in range(n):
            width = right[i] - left[i] - 1
            max_area = max(max_area, heights[i] * width)

        return max_area