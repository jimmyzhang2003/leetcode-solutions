# Link: https://leetcode.com/problems/valid-palindrome/
# Time Complexity: O(N)
# Space Complexity: O(1)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphanumeric = 'abcdefghijklmnopqrstuvwxyz0123456789'
        l, r = 0, len(s) - 1
        
        while l < r:
            if s[l].lower() not in alphanumeric:
                l += 1
                continue
            if s[r].lower() not in alphanumeric:
                r -= 1
                continue
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
            
        return True