from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        n = len(s)
        
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]
        
        def backtrack(start: int, path: List[str]):
            if start == n:
                res.append(path[:])
                return
            
            for end in range(start, n):
                substr = s[start:end+1]
                if is_palindrome(substr):
                    path.append(substr)
                    backtrack(end + 1, path)
                    path.pop()
        
        backtrack(0, [])
        return res
