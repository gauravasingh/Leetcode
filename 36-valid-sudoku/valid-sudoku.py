class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]  # Each index corresponds to a 3x3 sub-box

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                box_index = (r // 3) * 3 + (c // 3)

                if val in rows[r] or val in cols[c] or val in boxes[box_index]:
                    return False

                rows[r].add(val)
                cols[c].add(val)
                boxes[box_index].add(val)

        return True

