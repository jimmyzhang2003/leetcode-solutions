# Link: https://leetcode.com/problems/subtree-of-another-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(MN)
# Space Complexity: O(M + N)
# (DFS)
class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:
        def dfs1(root, subRoot):
            if not root and not subRoot:
                return True
            elif not root or not subRoot or root.val != subRoot.val:
                return False

            return dfs1(root.left, subRoot.left) and dfs1(root.right, subRoot.right)

        def dfs2(root):
            if not root:
                return
            
            if dfs1(root, subRoot):
                return True
            
            return dfs2(root.left) or dfs2(root.right)

        return dfs2(root)