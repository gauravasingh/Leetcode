from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        # Mapping of digits to letters
        phone = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        res = []

        def backtrack(index: int, path: str):
            # If the current path has the same length as digits, it's complete
            if index == len(digits):
                res.append(path)
                return
            
            # Get letters for current digit
            letters = phone[digits[index]]
            for letter in letters:
                backtrack(index + 1, path + letter)

        backtrack(0, "")
        return res
