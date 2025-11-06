class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # Add a zero at the end to ensure all bars are processed
        heights.append(0)
        stack = [-1]  # Sentinel index to simplify width calculation
        max_area = 0

        for i, h in enumerate(heights):
            # When the current bar is lower, compute area for taller bars
            while heights[stack[-1]] > h:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1
                max_area = max(max_area, height * width)
            stack.append(i)

        return max_area
