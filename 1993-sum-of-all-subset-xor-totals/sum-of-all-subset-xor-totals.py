class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        xor_all = 0
        for num in nums:
            xor_all |= num  # bitwise OR accumulates all bits that appear in any number
        
        # Each bit -> exactly half of all subsets (2^(n-1) times)
        return xor_all * (1 << (len(nums) - 1))
