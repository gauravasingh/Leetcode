from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = sum(nums)
        
        # Standard Kadane for max subarray
        def kadane(array):
            max_sum = array[0]
            curr = 0
            for num in array:
                curr = max(num, curr + num)
                max_sum = max(max_sum, curr)
            return max_sum
        
        max_nonwrap = kadane(nums)
        
        # Kadane for min subarray to find max_wrap
        min_sum = kadane([-num for num in nums])
        max_wrap = total + min_sum  # total - min_subarray_sum = total + (-min_sum)
        
        if max_wrap == 0:  # all numbers negative
            return max_nonwrap
        return max(max_nonwrap, max_wrap)
