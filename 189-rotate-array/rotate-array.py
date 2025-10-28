class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        n = len(nums)
        k %= n  # In case k > n

        # In-place reverse helper
        def reverse(l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                l += 1
                r -= 1

        # Reverse all, then first k, then the rest
        reverse(0, n - 1)
        reverse(0, k - 1)
        reverse(k, n - 1)
