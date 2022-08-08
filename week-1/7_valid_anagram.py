# Link: https://leetcode.com/problems/valid-anagram/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Hashmap)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letterDict = {}
        
        for letter in s:
            if letter in letterDict:
                letterDict[letter] += 1
            else:
                letterDict[letter] = 1
                
        for letter in t:
            if letter in letterDict and letterDict[letter] > 0:
                letterDict[letter] -= 1
            else:
                return False
            
        return sum(letterDict.values()) == 0