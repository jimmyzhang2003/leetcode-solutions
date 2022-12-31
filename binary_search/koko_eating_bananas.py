# Link: https://leetcode.com/problems/koko-eating-bananas/

# Time Complexity: O(N log N)
# Space Complexity: O(1)
# (Binary Search)
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = max(piles)

        while l <= r:
            mid = (l+r)//2
            totalTime = 0

            for num in piles:
                totalTime += math.ceil(num/mid)

            if totalTime > h:
                l = mid+1
            else:
                ans = min(ans, mid)
                r = mid-1

        return ans