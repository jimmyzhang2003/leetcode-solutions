# Link: https://leetcode.com/problems/contains-duplicate/description/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Hashset)
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for x in nums:
            if x in seen:
                return True
            seen.add(x)

        return False