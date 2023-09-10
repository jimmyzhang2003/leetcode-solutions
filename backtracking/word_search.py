# Link: https://leetcode.com/problems/word-search/

# Time Complexity: O(N * M * 4^(len(word)))
# Space Complexity: O(N * M)
# (DFS/Backtracking)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        def dfs(row, col, curr, idx):
            if len(curr) == len(word):
                return True

            for dx, dy in dirs:
                newX, newY = row + dx, col + dy

                if inBounds(newX, newY) and board[newX][newY] == word[idx]:
                    tmp = board[newX][newY]
                    board[newX][newY] = "$" # mark as visited
                    found = dfs(newX, newY, curr + [tmp], idx+1)
                    board[newX][newY]= tmp

                    if found:
                        return True
            
            return False

        def inBounds(row, col):
            return row >= 0 and col >= 0 and row < m and col < n
        
        # keep track of visited
        for row in range(m):
            for col in range(n):
                # start searching once we find the first letter of word
                if board[row][col] == word[0]:
                    tmp = board[row][col]
                    board[row][col] = "$"
                    found = dfs(row, col, [board[row][col]], 1)
                    board[row][col] = tmp

                    if found:
                        return True
        
        return False