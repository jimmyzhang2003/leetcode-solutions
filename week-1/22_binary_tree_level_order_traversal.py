# Link: https://leetcode.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Time Complexity: O(N)
# Space Complexity: O(N)
# (BFS)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        currLevel = []
        nextLevel = [root] if root else []
        
        while currLevel or nextLevel:
            if not currLevel:
                currLevel = nextLevel
                nextLevel = []
                res.append([node.val for node in currLevel])
            
            node = currLevel.pop(0)

            if node.left:
                nextLevel.append(node.left)
            if node.right:
                nextLevel.append(node.right)
        
        return res

# Time Complexity: O(N)
# Space Complexity: O(N)
# (BFS Alternative Solution)
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        currLevel = [root] if root else []
        
        while currLevel:
            res.append([node.val for node in currLevel])
            
            nextLevel = []
            
            for node in currLevel:
                nextLevel.extend([node.left, node.right])
            
            currLevel = [node for node in nextLevel if node]
            
        return res