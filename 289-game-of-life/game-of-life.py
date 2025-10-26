class Solution(object):
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if not board or not board[0]:
            return
        
        m, n = len(board), len(board[0])

        # Directions for the 8 neighbors
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),          (0, 1),
            (1, -1), (1, 0), (1, 1)
        ]

        # First pass: determine state transitions
        for i in range(m):
            for j in range(n):
                live_neighbors = 0

                # Count live neighbors
                for dx, dy in directions:
                    x, y = i + dx, j + dy
                    if 0 <= x < m and 0 <= y < n and abs(board[x][y]) == 1:
                        live_neighbors += 1

                # Rule 1 or 3: live cell dies
                if board[i][j] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[i][j] = -1  # 1 → 0 (mark as dead but was alive)
                # Rule 4: dead cell becomes live
                if board[i][j] == 0 and live_neighbors == 3:
                    board[i][j] = 2   # 0 → 1 (mark as live but was dead)

        # Second pass: finalize new states
        for i in range(m):
            for j in range(n):
                if board[i][j] > 0:
                    board[i][j] = 1
                else:
                    board[i][j] = 0
