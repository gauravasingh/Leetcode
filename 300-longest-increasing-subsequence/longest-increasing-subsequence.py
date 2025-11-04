import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        for x in nums:
            i = bisect.bisect_left(sub, x)
            if i < len(sub):
                sub[i] = x
            else:
                sub.append(x)
        return len(sub)
