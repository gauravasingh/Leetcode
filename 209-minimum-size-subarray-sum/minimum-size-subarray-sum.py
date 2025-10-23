class Solution(object):
    def minSubArrayLen(self, target, nums):
        # Edge case: if the array is empty return 0
        if not nums:
            return 0
        
        n = len(nums)
        min_len = float('inf')  # Set to infinity initially will track the minimal length
        current_sum = 0  # Current sum of the sliding window
        left = 0  # Left pointer of the window
        
        for right in range(n):
            current_sum += nums[right]
            
            # Once the sum is >= target, try to minimize the window
            while current_sum >= target:
                min_len = min(min_len, right - left + 1)  # Update minimal length
                current_sum -= nums[left]  # Shrink window from the left
                left += 1  # Move left pointer to the right
            
        return min_len if min_len != float('inf') else 0  # If no valid subarray return 0
