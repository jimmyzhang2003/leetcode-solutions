# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

# Time Complexity: O(N)
# Space Complexity: O(1)
# (Sliding Window)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        l, r = 0, 1

        while r < len(prices):
            profit = max(profit, prices[r] - prices[l])
            
            if prices[r] < prices[l]:
                l = r
                
            r += 1

        return profit

# Time Complexity: O(N)
# Space Complexity: O(1)
# (Kadane's Algorithm)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        currMin = prices[0]
        
        for i in range(1, len(prices)):
            currMin = min(currMin, prices[i])
            profit = max(profit, prices[i]-currMin)
            
        return profit