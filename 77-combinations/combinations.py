from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(start: int, path: List[int]):
            # If the path has k numbers, add it to the result
            if len(path) == k:
                res.append(path[:])
                return
            
            # Try adding each number from start to n
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)  # move to next number
                path.pop()  # backtrack
        
        backtrack(1, [])
        return res
