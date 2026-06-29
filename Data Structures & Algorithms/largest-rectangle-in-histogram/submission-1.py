class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        area = 0
        for i in range(len(heights)):
            while stack and heights[i]<=heights[stack[-1]]:
                mid = stack.pop()
                right = i
                left = stack[-1] if stack else -1
                width = right-left-1
                area = max(area, width*heights[mid])
            stack.append(i)
        while stack:
            mid = stack.pop()
            right = len(heights)
            left = stack[-1] if stack else -1
            width = right-left-1
            area = max(area, width*heights[mid])
        return area