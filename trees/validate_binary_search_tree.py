# Link: https://leetcode.com/problems/validate-binary-search-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N) 
# (Binary Search Tree / In-Order Traversal / DFS (Iterative))
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        stack = []
        prev = None
        
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            
            root = stack.pop()
            
            if prev and root.val <= prev.val:
                return False
            
            prev = root
            root = root.right
        
        return True

# Time Complexity: O(N)
# Space Complexity: O(N) 
# (Binary Search Tree / DFS (Recursive))
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, low, high):
            if not root:
                return True
            
            if root.val <= low or root.val >= high:
                return False
            
            return dfs(root.left, low, root.val) and dfs(root.right, root.val, high)
            
        return dfs(root, float('-inf'), float('inf'))