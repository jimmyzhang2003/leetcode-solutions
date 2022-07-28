# Link: https://leetcode.com/problems/flood-fill/
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        stack = [(sr, sc)]
        startColor = image[sr][sc]
        visited = [len(image[0]) * [0] for _ in range(len(image))]
        
        while len(stack) > 0:
            x, y = stack.pop()
            
            if x >= 0 and x < len(image) and y >= 0 and y < len(image[0]) and not visited[x][y] and image[x][y] == startColor:
                visited[x][y] = 1
                image[x][y] = color
                stack.extend([(x-1, y), (x+1, y), (x, y-1), (x, y+1)])
            
        return image   