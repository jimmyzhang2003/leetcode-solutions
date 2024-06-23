# Link: https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(log N) or O(h)
# (DFS)
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(root, currMax):
            if not root:
                return 0

            newMax = max(currMax, root.val)
            
            return (root.val >= currMax) + dfs(root.left, newMax) + dfs(root.right, newMax)

        return dfs(root, float('-inf'))