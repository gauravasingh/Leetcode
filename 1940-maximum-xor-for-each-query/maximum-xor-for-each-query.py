class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        mask = (1 << maximumBit) - 1
        xor_all = 0
        for num in nums:
            xor_all ^= num

        res = []
        for num in reversed(nums):
            res.append(mask ^ xor_all)
            xor_all ^= num
        return res
