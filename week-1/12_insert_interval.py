# Link: https://leetcode.com/problems/insert-interval/
# Time Complexity: O(N)
# Space Complexity: O(N)

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:     
        out = []
        
        for i, x in enumerate(intervals):
            if newInterval[0] > x[1]:
                out.append(x)
            elif newInterval[1] < x[0]:
                out.append(newInterval)
                return out + intervals[i:]
            else:
                newStart = min(newInterval[0], x[0])
                newEnd = max(newInterval[1], x[1])
                newInterval = [newStart, newEnd]
                
        return out + [newInterval]