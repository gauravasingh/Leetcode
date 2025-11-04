from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            # If mid element is less than next element, peak must be on the right
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else:
                # Peak is on the left or it is mid itself
                right = mid

        return left  # or right, both are equal here

# Example usage:
nums = [1, 2, 3, 1]
print(Solution().findPeakElement(nums))  # Output: 2 (index of peak 3)
