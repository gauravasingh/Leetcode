class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set(nums)
        
        for num in nums:
            rev = int(str(num)[::-1])
            seen.add(rev)
        
        return len(seen)