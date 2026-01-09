from typing import List

class SubrectangleQueries:

    def __init__(self, rectangle: List[List[int]]):
        # Store the rectangle
        self.rectangle = rectangle

    def updateSubrectangle(
        self, row1: int, col1: int, row2: int, col2: int, newValue: int
    ) -> None:
        # Update all cells in the specified subrectangle
        for r in range(row1, row2 + 1):
            for c in range(col1, col2 + 1):
                self.rectangle[r][c] = newValue

    def getValue(self, row: int, col: int) -> int:
        # Return the value at the specified cell
        return self.rectangle[row][col]

# Your SubrectangleQueries object will be instantiated and called as such:
# obj = SubrectangleQueries(rectangle)
# obj.updateSubrectangle(row1,col1,row2,col2,newValue)
# param_2 = obj.getValue(row,col)