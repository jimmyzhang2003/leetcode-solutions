# Link: https://leetcode.com/problems/coin-change/

# Time Complexity: O(N * A)
# Space Complexity: O(A)
# (DP (Top-Down))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        def coinChangeRecursive(coins, amount, memo):
            if amount == 0:
                return 0
        
            if amount < 0:
                return float('inf')
            
            if memo[amount] != float('inf'):
                return memo[amount]
            
            memo[amount] = min(1 + coinChangeRecursive(coins, amount - coin, memo) for coin in coins)
                    
            return memo[amount]
            
        memo = [0] + [float('inf') for _ in range(amount)]
        ans = coinChangeRecursive(coins, amount, memo)
        
        return ans if ans != float('inf') else -1

# Time Complexity: O(N * A)
# Space Complexity: O(A)
# (DP (Bottom-Up))
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int: 
        dp = [0] + [float('inf') for _ in range(amount)]
        
        for i in range(1, amount + 1):      
            for coin in coins:
                if coin <= amount:
                    dp[i] = min(dp[i], 1 + dp[i-coin])
                    
        return dp[amount] if dp[amount] != float('inf') else -1