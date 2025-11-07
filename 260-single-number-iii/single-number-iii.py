class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 1: XOR all numbers → gives xor = a ⊕ b
        xor = 0
        for num in nums:
            xor ^= num

        # 2: Find a diff bit (rightmost set bit)
        diff_bit = xor & -xor

        # 3: Split numbers into two groups and XOR separately
        a = 0
        b = 0
        for num in nums:
            if num & diff_bit:
                a ^= num
            else:
                b ^= num

        return [a, b]
