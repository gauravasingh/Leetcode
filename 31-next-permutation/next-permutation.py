class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        
        """
        n = len(nums)
        
        # Finding the first decreasing element from the right
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # If such an element exists, finding the next larger element to swap with
        if i >= 0:
            j = n - 1
            while nums[j] <= nums[i]:
                j -= 1
            nums[i], nums[j] = nums[j], nums[i]
        
        # Reversing the suffix to get the smallest possible order
        nums[i + 1:] = reversed(nums[i + 1:])
