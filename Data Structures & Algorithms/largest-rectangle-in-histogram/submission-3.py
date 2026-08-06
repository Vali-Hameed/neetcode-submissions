class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        n = len(heights)
        left = [0] * n
        right = [n - 1] * n
        
        # Pass 1: Find left boundaries
        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] + 1 if stack else 0
            stack.append(i)
            
        # Pass 2: Find right boundaries
        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] - 1 if stack else n - 1
            stack.append(i)
            
        # Compute maximum area
        max_area = 0
        for i in range(n):
            width = right[i] - left[i] + 1
            max_area = max(max_area, heights[i] * width)
            
        return max_area