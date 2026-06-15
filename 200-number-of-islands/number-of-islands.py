class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        M = len(grid)
        N = len(grid[0])
        islands = 0
        DIRECTIONS = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def dfs(r, c):
            for dr, dc in DIRECTIONS:
                new_r, new_c = r + dr, c + dc    
                if new_r in range(M) and new_c in range(N) and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                    visited.add((new_r, new_c))
                    dfs(new_r, new_c)
        
        for row in range(M):
            for col in range(N):
                if (row, col) not in visited and grid[row][col] == '1':
                    visited.add((row, col))
                    dfs(row, col)
                    islands += 1
        
        return islands
            
                

