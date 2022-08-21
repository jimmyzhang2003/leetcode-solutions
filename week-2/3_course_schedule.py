# Link: https://leetcode.com/problems/course-schedule/

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# (DFS Topological Sort (with Stack))
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        reqs = {i : [] for i in range(numCourses)}
        indegrees = [0 for i in range(numCourses)]
        
        for course1, course2 in prerequisites:
            reqs[course2].append(course1)
            indegrees[course1] += 1
            
        stack = [i for i in range(numCourses) if indegrees[i] == 0]
        
        while stack:
            course = stack.pop()
            
            for req in reqs[course]:
                indegrees[req] -= 1
                
                if indegrees[req] == 0:
                    stack.append(req)
        
        return sum(indegrees) == 0

# Time Complexity: O(V + E)
# Space Complexity: O(V + E)
# (Recursive DFS)
class Solution:
    def canFinish(self, numCourses, prerequisites):
        def dfs(reqs, visited, i):
            # if node is being visited, then there is a cycle
            if visited[i] == -1:
                return False
            # if node is done visited, don't visit again
            if visited[i] == 1:
                return True
            # mark node as being visited
            visited[i] = -1       
            # visit neighbors
            for j in reqs[i]:
                if not dfs(reqs, visited, j):
                    return False
            
            # mark node as done visited
            visited[i] = 1
    
            return True
        
        reqs = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]

        for course1, course2 in prerequisites:
            reqs[course1].append(course2)

        for i in range(numCourses):
            if not dfs(reqs, visited, i):
                return False
        
        return True