# Link: https://leetcode.com/problems/subsets/

# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# (Backtracking)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr, res):
            if idx > len(nums):
                return
                
            res.append(curr)

            for i in range(idx, len(nums)):
                backtrack(i+1, curr + [nums[i]], res)

        res = []
        backtrack(0, [], res)
        
        return res

# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# (Backtracking Alternative Solution)
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr, res):
            res.append(curr.copy())

            for i in range(idx, len(nums)):
                curr.append(nums[i])
                backtrack(i+1, curr, res)
                curr.pop()

        res = []
        backtrack(0, [], res)

        return res