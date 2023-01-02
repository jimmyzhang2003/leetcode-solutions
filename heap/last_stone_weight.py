# Link: https://leetcode.com/problems/last-stone-weight/

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# (Heap)
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-weight for weight in stones]
        heapq.heapify(stonesHeap)

        while stonesHeap:
            y = heapq.heappop(stonesHeap)

            if not stonesHeap:
                return -y

            x = heapq.heappop(stonesHeap)
            
            if x != y:
                heapq.heappush(stonesHeap, y-x)

        return 0

# Time Complexity: O(N log N)
# Space Complexity: O(N)
# (Heap Alternative Solution)
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stonesHeap = [-weight for weight in stones]
        heapq.heapify(stonesHeap)

        while len(stonesHeap) > 1:
            heapq.heappush(stonesHeap, heapq.heappop(stonesHeap)-heapq.heappop(stonesHeap))

        return -stonesHeap[0]