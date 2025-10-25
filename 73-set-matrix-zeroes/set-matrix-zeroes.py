class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = False
        first_col_zero = False

        # 1: Determine if first row or column should be zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True

        #2 Use first row and first column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # 3:Set matrix cells to 0 using markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # 4-Handle the first row and first column separately
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0
