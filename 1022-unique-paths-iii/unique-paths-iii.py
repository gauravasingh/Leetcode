class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        
        # Count total cells that must be visited (all except -1)
        total_to_visit = 0
        start = None
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] != -1:
                    total_to_visit += 1
                if grid[i][j] == 1:
                    start = (i, j)
        
        # DFS 
        def dfs(x, y, visited_count):
            # If we reached the ending square
            if grid[x][y] == 2:
                # Check if all non-obstacle cells were visited
                return 1 if visited_count == total_to_visit else 0
            
            # Temp for visited
            temp = grid[x][y]
            grid[x][y] = -1  # mark as obstacle to stop revisiting
            
            total_paths = 0
            directions = [(1,0), (-1,0), (0,1), (0,-1)]
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != -1:
                    total_paths += dfs(nx, ny, visited_count + 1)
            
            # Backtrack
            grid[x][y] = temp
            
            return total_paths
        
        # DFS from the starting cell
        sx, sy = start
        return dfs(sx, sy, 1)
