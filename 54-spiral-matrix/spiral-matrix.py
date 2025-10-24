class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        res = []
        if not matrix:
            return res
        
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        
        while top <= bottom and left <= right:
            # Traverse from Left → Right
            for j in range(left, right + 1):
                res.append(matrix[top][j])
            top += 1
            
            # Traverse from Top → Bottom
            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1
            
            # Traverse from Right → Left
            if top <= bottom:
                for j in range(right, left - 1, -1):
                    res.append(matrix[bottom][j])
                bottom -= 1
            
            # Traverse from Bottom → Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1
        
        return res
