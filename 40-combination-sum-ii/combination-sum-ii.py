from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        results = []

        def backtrack(start: int, path: List[int], remaining: int):
            if remaining == 0:
                results.append(path[:])
                return

            for i in range(start, len(candidates)):
                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Stopping if current number is greater than remaining target
                if candidates[i] > remaining:
                    break

                path.append(candidates[i])
                backtrack(i + 1, path, remaining - candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], target)
        return results
