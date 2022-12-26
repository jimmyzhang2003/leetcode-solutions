# Link: https://leetcode.com/problems/climbing-stairs/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (DP (Top-Down))
class Solution:
    def climbStairs(self, n: int) -> int:
        def dp(n, memo):
            if n < 0:
                return 0
            
            if n == 0:
                return 1
            
            if memo[n]:
                return memo[n]
            
            memo[n] = dp(n-1, memo) + dp(n-2, memo)
            
            return memo[n]      
            
        memo = [None for _ in range(n+1)]
        
        return dp(n, memo)

# Time Complexity: O(N)
# Space Complexity: O(1)
# (DP (Bottom-Up))
class Solution:
    def climbStairs(self, n: int) -> int:
        p1, p2 = 1, 1
        
        for i in range(2, n+1):
            p3 = p1 + p2
            p1, p2 = p2, p3
            
        return p2