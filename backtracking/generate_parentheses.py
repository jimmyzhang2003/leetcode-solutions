# Link: https://leetcode.com/problems/generate-parentheses/

# Time Complexity: O(4^N / √N)
# Space Complexity: O(4^N / √N)
# (Backtracking)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(nLeft, nRight, res, curr):
            if not nLeft:
                res.append("".join(curr) + nRight * ")")
                return

            backtrack(nLeft-1, nRight, res, curr + ["("])

            if nRight > nLeft:
                backtrack(nLeft, nRight-1, res, curr + [")"])

        res = []
        backtrack(n, n, res, [])

        return res