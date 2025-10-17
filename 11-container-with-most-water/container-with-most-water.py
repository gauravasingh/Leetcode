class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            width = right - left
            max_area = max(max_area, min(left_height, right_height) * width)

            if left_height < right_height:
            
                while left < right and height[left] <= left_height:
                    left += 1
            else:
                while left < right and height[right] <= right_height:
                    right -= 1

        return max_area


        