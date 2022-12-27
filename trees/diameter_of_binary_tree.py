# Link: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
# (DFS)
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def dfs(root):
            if not root:
                return 0

            lBest = dfs(root.left)
            rBest = dfs(root.right)

            self.best = max(self.best, lBest + rBest)

            return max(lBest, rBest) + 1

        dfs(root)
        return self.best