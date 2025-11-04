class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        for i in range(32):  # iterate over each bit position
            bit_count = 0
            for num in nums:
                # count how many numbers have the i-th bit set
                if (num >> i) & 1:
                    bit_count += 1
            # the bit in the single number is bit_count % 3
            if bit_count % 3:
                # handle negative numbers for 32-bit signed integer
                if i == 31:  # sign bit
                    result -= (1 << i)
                else:
                    result |= (1 << i)
        return result
