# Link: https://leetcode.com/problems/group-anagrams/

# Time Complexity: O(N K log K)
# Space Complexity: O(NK)
# (Hashset and Sorting)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs: 
            anagrams["".join(sorted(word))].append(word)

        return anagrams.values()

# Time Complexity: O(NK)
# Space Complexity: O(NK)
# (Hashset and Sorting Optimized)
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for word in strs:
            # use tuple of character counts as key
            counts = [0] * 26

            for letter in word:
                counts[ord(letter) - ord('a')] += 1

            anagrams[tuple(counts)].append(word)

        return anagrams.values()
                