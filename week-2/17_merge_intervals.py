# Link: https://leetcode.com/problems/merge-intervals/

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# (Array / Sorting)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start element
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            tmpInterval = res.pop()
            
            if tmpInterval[1] >= intervals[i][0]:
                tmpInterval = [tmpInterval[0], max(tmpInterval[1], intervals[i][1])]
                res.append(tmpInterval)
            else:
                res.append(tmpInterval)
                res.append(intervals[i])
            
        return res

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# (Array / Sorting Alternative Solution)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by start element
        intervals.sort(key=lambda x: x[0])
        
        res = [intervals[0]]
        
        for i in range(1, len(intervals)):
            if res[-1][1] >= intervals[i][0]:
                res[-1] = [res[-1][0], max(res[-1][1], intervals[i][1])]
            else:
                res.append(intervals[i])
            
        return res