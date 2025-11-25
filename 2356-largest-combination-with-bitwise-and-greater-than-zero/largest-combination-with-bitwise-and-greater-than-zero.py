class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        bit_count = [0] * 24  # enough for values up to 1e7
        
        for num in candidates:
            for bit in range(24):
                if num & (1 << bit):
                    bit_count[bit] += 1
        
        return max(bit_count)
