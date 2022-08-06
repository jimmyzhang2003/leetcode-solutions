# Link: https://leetcode.com/problems/01-matrix/
# Time Complexity: O(N * M)
# Space Complexity: O(N * M)

## BFS
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        out = [[float('inf')] * len(mat[0]) for _ in range(len(mat))]
        queue = []
        
        #add all 0s to the queue
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    out[i][j] = 0
                    queue.append([i,j])
    
        #then do BFS
        dirs = [[-1, 0], [0, -1], [0, 1], [1, 0]]
        while queue:
            cell = queue.pop(0)
            
            for i in range(4):
                x, y = cell[0] + dirs[i][0], cell[1] + dirs[i][1]
                
                if x >= 0 and x < len(mat) and y >= 0 and y < len(mat[0]) and out[cell[0]][cell[1]] + 1 < out[x][y]:
                    out[x][y] = out[cell[0]][cell[1]] + 1
                    queue.append([x, y])
            
        return out


## DP: O(1) space complexity
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        #checking top and left neighbors
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    continue
                top = mat[i-1][j] if i-1 >= 0 else float('inf')
                left = mat[i][j-1] if j-1 >= 0 else float('inf')
                mat[i][j] = min(top, left) + 1
                
        #checking bottom and right neighbors
        for i in reversed(range(len(mat))):
            for j in reversed(range(len(mat[0]))):
                if mat[i][j] == 0:
                    continue
                bottom = mat[i+1][j] if i+1 < len(mat) else float('inf')
                right = mat[i][j+1] if j+1 < len(mat[0]) else float('inf')
                mat[i][j] = min(mat[i][j], min(bottom, right) + 1)
                
        return mat