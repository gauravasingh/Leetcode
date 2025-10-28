class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # handle large k

        # Func to reverse part of array
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # 1: Reverse the entire array
        reverse(0, n - 1)
        # 2: Reverse the first k elements
        reverse(0, k - 1)
        #  3: Reverse the rest
        reverse(k, n - 1)
# a