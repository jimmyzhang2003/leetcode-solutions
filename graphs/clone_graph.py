# Link: https://leetcode.com/problems/clone-graph/

"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

# Time Complexity: O(V + E)
# Space Complexity: O(V)
# (BFS)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        queue = [node]
        clonedGraph = {node.val : Node(node.val, [])}
        
        while queue:
            curr = queue.pop(0)
            currClone = clonedGraph[curr.val]
            
            for neighbor in curr.neighbors:
                if neighbor.val not in clonedGraph:
                    clonedGraph[neighbor.val] = Node(neighbor.val, [])
                    queue.append(neighbor)
                    
                currClone.neighbors.append(clonedGraph[neighbor.val])
        
        return clonedGraph[node.val]

# Time Complexity: O(V + E)
# Space Complexity: O(V)
# (Recursive DFS)
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        def dfs(node, graph):
            if node.val in clonedGraph:
                return clonedGraph[node.val]
            
            clone = Node(node.val, [])
            clonedGraph[node.val] = clone
            
            for x in node.neighbors:
                clonedGraph[node.val].neighbors.append(dfs(x, clonedGraph))
                
            return clone
        
        clonedGraph = {}
        
        return dfs(node, clonedGraph) if node else node