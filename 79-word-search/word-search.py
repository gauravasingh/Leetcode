from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def dfs(r, c, i):
            # If all characters are matched
            if i == len(word):
                return True
            # If out of bounds or mismatch
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            
            # Mark the cell as visited
            temp = board[r][c]
            board[r][c] = "#"

            # Explore all four directions
            found = (dfs(r+1, c, i+1) or
                     dfs(r-1, c, i+1) or
                     dfs(r, c+1, i+1) or
                     dfs(r, c-1, i+1))

            # Restore the cell (backtrack)
            board[r][c] = temp
            return found

        # Try starting from every cell that matches the first letter
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0] and dfs(r, c, 0):
                    return True
        
        return False
