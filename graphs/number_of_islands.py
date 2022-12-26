# Link: https://leetcode.com/problems/number-of-islands/

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# (DFS)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j, visited):
            if visited[i][j]:
                return
            
            visited[i][j] = 1
            
            if grid[i][j] == "0":
                return
            
            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for x, y in dirs:
                newX = i + x
                newY = j + y
                
                if inBounds(newX, newY, grid):
                    dfs(grid, newX, newY, visited)
            
            return 1
        
        def inBounds(x, y, grid):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        
        visited = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if dfs(grid, i, j, visited):
                    numIslands += 1

        return numIslands

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# (DFS (modifying input grid directly))
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(grid, i, j):
            if grid[i][j] == "0":
                return
            
            grid[i][j] = "0"
            
            dirs = [[-1, 0], [0, -1], [1, 0], [0, 1]]
            
            for x, y in dirs:
                newX = i + x
                newY = j + y
                
                if inBounds(newX, newY, grid):
                    dfs(grid, newX, newY)
        
        def inBounds(x, y, grid):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        
        numIslands = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(grid, i, j)
                    numIslands += 1

        return numIslands