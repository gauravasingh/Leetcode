from collections import deque

class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        n = len(board)

        # Helper to convert cell number → (row, col)
        def get_position(square):
            # Convert to 0-based index
            r = n - 1 - (square - 1) // n
            c = (square - 1) % n
            # Reverse direction every other row
            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c
            return r, c

        visited = set()
        queue = deque([(1, 0)])  # (square, moves)
        visited.add(1)

        while queue:
            square, moves = queue.popleft()
            if square == n * n:
                return moves  # reached the end

            for step in range(1, 7):  # simulate dice roll (1–6)
                next_square = square + step
                if next_square > n * n:
                    break
                r, c = get_position(next_square)
                if board[r][c] != -1:
                    next_square = board[r][c]  # follow snake or ladder
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1  # unreachable
