# Link: https://leetcode.com/problems/pacific-atlantic-water-flow/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (DFS)
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        def dfs(r, c, visited):
            if visited[r][c]:
                return

            visited[r][c] = 1

            for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                newX, newY = r+dx, c+dy

                if inBounds(newX, newY) and heights[r][c] <= heights[newX][newY]:
                    dfs(newX, newY, visited)

        def inBounds(r, c):
            return r >= 0 and c >= 0 and r < nRows and c < nCols

        nRows, nCols = len(heights), len(heights[0])
        atlanticVisited = [[0 for _ in range(nCols)] for _ in range(nRows)]
        pacificVisited = [[0 for _ in range(nCols)] for _ in range(nRows)]

        for r in range(nRows):
            # pacific ocean from left
            dfs(r, 0, pacificVisited)

            # atlantic ocean from right
            dfs(r, nCols-1, atlanticVisited)
        
        for c in range(nCols):
            # pacific ocean from top
            dfs(0, c, pacificVisited)

            # atlantic ocean from bottom
            dfs(nRows-1, c, atlanticVisited)

        result = []

        for r in range(nRows):
            for c in range(nCols):
                if pacificVisited[r][c] and atlanticVisited[r][c]:
                    result.append([r, c])

        return result