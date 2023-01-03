# Link: https://leetcode.com/problems/subsets-ii/

# Time Complexity: O(N * 2^N)
# Space Complexity: O(N)
# (Backtracking)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(idx, curr, res):
            res.append(curr.copy())

            for i in range(idx, len(nums)):
                if i > idx and nums[i] == nums[i-1]:
                    continue

                curr.append(nums[i])
                backtrack(i+1, curr, res)
                curr.pop()

        nums.sort()
        res = []
        backtrack(0, [], res)

        return res