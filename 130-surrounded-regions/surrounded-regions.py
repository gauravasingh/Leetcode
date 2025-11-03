class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        
        rows, cols = len(board), len(board[0])
        
        def dfs(r, c):
            # Stop if out of bounds or not 'O'
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != 'O':
                return
            # Mark as safe (connected to border)
            board[r][c] = 'S'
            # Explore 4 directions
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+1)
            dfs(r, c-1)
        
        # 1️⃣ Step 1: Mark all 'O's on the border and connected to the border as safe
        for r in range(rows):
            for c in range(cols):
                if (r in [0, rows-1] or c in [0, cols-1]) and board[r][c] == 'O':
                    dfs(r, c)
        
        # 2️⃣ Step 2: Flip all remaining 'O's → 'X' (these are surrounded)
        # and flip all 'S' → 'O' (restore safe regions)
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'S':
                    board[r][c] = 'O'
