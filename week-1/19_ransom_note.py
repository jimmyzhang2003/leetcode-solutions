# Link: https://leetcode.com/problems/ransom-note/

# Time Complexity: O(N + M)
# Space Complexity: O(1)
# (Hashmap)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        
        for x in magazine:
            if x not in letters:
                letters[x] = 1
            else:
                letters[x] += 1
                
        for x in ransomNote:
            if x not in letters or letters[x] == 0:
                return False
            else:
                letters[x] -= 1
        
        return True