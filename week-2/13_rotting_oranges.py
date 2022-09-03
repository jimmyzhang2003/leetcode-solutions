# Link: https://leetcode.com/problems/rotting-oranges/

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# (BFS)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inBounds(x, y, grid):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        
        queue = []
        minutes = 0
        
        # add all rotten oranges into the queue
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append([i, j])
    
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue:
            nextLevel = []
            
            for orange in queue:
                if grid[orange[0]][orange[1]] == -1:
                    continue
                    
                for dir in dirs:
                    nextOrange = [orange[0] + dir[0], orange[1] + dir[1]]
                
                    # only add if in bounds and is a fresh orange
                    if inBounds(nextOrange[0], nextOrange[1], grid) and grid[nextOrange[0]][nextOrange[1]] == 1:
                        grid[nextOrange[0]][nextOrange[1]] = 2
                        nextLevel.append(nextOrange)
                        
                # set to visited (-1)
                grid[orange[0]][orange[1]] = -1
              
            if nextLevel:
                minutes += 1
                
            queue = nextLevel
        
        # make sure there are no more fresh oranges after the bfs
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return minutes

# Time Complexity: O(N * M)
# Space Complexity: O(N * M)
# (BFS Alternative Solution)
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        def inBounds(x, y, grid):
            return x >= 0 and x < len(grid) and y >= 0 and y < len(grid[0])
        
        queue = []
        freshOranges = 0
        minutes = 0
        
        # add all rotten oranges into the queue and keep track of fresh oranges
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    freshOranges += 1
                if grid[i][j] == 2:
                    queue.append([i, j])
    
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        while queue and freshOranges > 0:
            nextLevel = []
            minutes += 1
            
            for _ in range(len(queue)):
                x, y = queue.pop(0)
                    
                for dx, dy in dirs:
                    xx, xy = x + dx, y + dy

                    # only add if in bounds and is a fresh orange
                    if inBounds(xx, xy, grid) and grid[xx][xy] == 1:
                        freshOranges -= 1
                        grid[xx][xy] = 2
                        nextLevel.append([xx, xy])
                
            queue = nextLevel
            
        return minutes if freshOranges == 0 else -1