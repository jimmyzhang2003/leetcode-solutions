# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currMax = 0
        b, s = 0, 1
    
        while s < len(prices):
            currMax = max(currMax, prices[s] - prices[b])
            
            if prices[b] > prices[s]:
                b = s
            
            s += 1    
    
        return currMax