from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int], total: int):
            # If the current total equals the target, record the combination
            if total == target:
                res.append(path[:])
                return
            # If total exceeds target, stop exploring
            if total > target:
                return
            
            # Try each candidate starting from 'start' (to avoid duplicates)
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                # You can reuse the same number, so 'i' stays the same
                backtrack(i, path, total + candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return res
