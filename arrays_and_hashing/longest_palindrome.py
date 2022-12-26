# Link: https://leetcode.com/problems/climbing-stairs/

# Time Complexity: O(N)
# Space Complexity: O(M) -> bounded by the size of the charset
# (Hashset)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = 0
        used = set()
        
        for x in s:
            if x not in used:
                used.add(x)
            else:
                length += 2
                used.remove(x)
        
        return length if not used else length + 1