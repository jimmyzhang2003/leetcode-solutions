# Link: https://leetcode.com/problems/balanced-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N^2)
# Space Complexity: O(N)
# (DFS (Top-Down))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def getHeight(root: Optional[TreeNode]):
            if not root:
                return 0
            
            return 1 + max(getHeight(root.left), getHeight(root.right))

        if not root:
            return True
        
        return abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

# Time Complexity: O(N)
# Space Complexity: O(N)
# (DFS (Bottom-Up))
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(root: Optional[TreeNode]):
            if not root:
                return 0

            leftHeight = dfs(root.left)
            rightHeight = dfs(root.right)

            if leftHeight == -1 or rightHeight == -1 or abs(leftHeight - rightHeight) > 1:
                return -1

            return 1 + max(leftHeight, rightHeight)
    
        return dfs(root) != -1
