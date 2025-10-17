class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            current_height = min(height[left], height[right])
            current_width = right - left
            current_area = current_height * current_width
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

        