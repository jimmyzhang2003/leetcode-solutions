# Link: https://leetcode.com/problems/longest-substring-without-repeating-characters/

# Time Complexity: O(N)
# Space Complexity: O(M) -> bounded by size of the charset
# (Hashset/Sliding Window)
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLength = currLength = 0
        used = set()
        start = 0
        
        for x in s:
            if x not in used:
                used.add(x)
                currLength += 1
                maxLength = max(maxLength, currLength)
            else:
                while start < len(s) and s[start] != x:
                    used.remove(s[start])
                    start += 1
                    currLength -= 1
                start += 1
        
        return maxLength

# Time Complexity: O(N)
# Space Complexity: O(M) -> bounded by size of the charset
# (Hashmap/Sliding Window) -> optimized by keeping track of indices
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = {}
        l = 0
        maxLength = 0
        
        for r in range(len(s)):
            if s[r] in used:
                l = max(used[s[r]] + 1, l)
                
            maxLength = max(maxLength, r - l + 1)
            used[s[r]] = r
                
        return maxLength