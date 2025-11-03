from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(path: List[int], remaining: List[int]):
            # If no numbers remain, add the current permutation to the result
            if not remaining:
                res.append(path[:])
                return
            
            # Try each remaining number in the current position
            for i in range(len(remaining)):
                path.append(remaining[i])
                backtrack(path, remaining[:i] + remaining[i+1:])  # remove used number
                path.pop()  # backtrack

        backtrack([], nums)
        return res
