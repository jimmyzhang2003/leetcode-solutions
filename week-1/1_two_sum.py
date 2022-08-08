# Link: https://leetcode.com/problems/two-sum/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Hashmap)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        
        for i, x in enumerate(nums):
            if target - x in seen:
                return [i, seen[target-x]]
            seen[x] = i
        
        return []