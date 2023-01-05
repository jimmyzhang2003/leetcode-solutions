# Link: https://leetcode.com/problems/longest-repeating-character-replacement/

# Time Complexity: O(N)
# Space Complexity: O(M) -> depends on size of alphabet
# (Sliding Window)
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = l = 0
        letterCounts = defaultdict(int)

        for r in range(len(s)):
            letterCounts[s[r]] += 1

            # check if valid substring (with replacements)
            if r - l + 1 - max(letterCounts.values()) <= k:
                ans = max(ans, r - l + 1)
            else: # otherwise, move left pointer until we have valid substring again
                while r - l + 1 - max(letterCounts.values()) > k:
                    letterCounts[s[l]] -= 1
                    l += 1
                    
        return ans

# Time Complexity: O(N)
# Space Complexity: O(M) -> depends on size of alphabet
# (Sliding Window Optimized)
from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = l = 0
        letterCounts = defaultdict(int)
        maxFreq = 0

        for r in range(len(s)):
            letterCounts[s[r]] += 1
            maxFreq = max(maxFreq, letterCounts[s[r]])

            # check if valid substring (with replacements)
            if r - l + 1 - maxFreq <= k:
                ans = max(ans, r - l + 1)
            else: # otherwise, move left pointer until we have valid substring again
                while r - l + 1 - maxFreq > k:
                    letterCounts[s[l]] -= 1
                    l += 1
                    
        return ans