# Link: https://leetcode.com/problems/first-bad-version/

# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

# Time Complexity: O(log N)
# Space Complexity: O(1)
# (Binary Search)
class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        
        while l <= r:
            mid = (l + r) // 2
            
            if isBadVersion(mid):
                r = mid - 1
            else:
                l = mid + 1
                
        return l