# Link: https://leetcode.com/problems/combination-sum/

# Time Complexity: O(2^T * K)
# Space Complexity: O(K * X)
# (Backtracking)
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(candidates, target, res, currSol, idx):
            if target < 0 or idx >= len(candidates):
                return
                
            if target == 0:
                res.append(currSol)
                return
            
            for i in range(idx, len(candidates)):
                backtrack(candidates, target - candidates[i], res, currSol + [candidates[i]], i)
                
        res = []
        
        backtrack(candidates, target, res, [], 0)
        
        return res