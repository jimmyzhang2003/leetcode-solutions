# Link: https://leetcode.com/problems/permutations/

# Time Complexity: O(N * N!)
# Space Complexity: O(N!)
# (Backtracking)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, curr):
            if len(curr) == len(nums):
                res.append(curr)
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    backtrack(nums, res, curr + [nums[i]])

        res = []
        
        backtrack(nums, res, [])
        
        return res

# Time Complexity: O(N * N!)
# Space Complexity: O(N!)
# (Backtracking Alternative Solution)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(nums, res, curr):
            if len(curr) == len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] not in curr:
                    curr.append(nums[i])
                    backtrack(nums, res, curr)
                    curr.pop()

        res = []
        
        backtrack(nums, res, [])
        
        return res