# Link: https://leetcode.com/problems/k-closest-points-to-origin/
# Time Complexity: O(N log K)
# Space Complexity: O(K)

## Max Heap
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = -(x ** 2 + y ** 2)
            
            if len(heap) == k:
                heapq.heappushpop(heap, [dist, [x,y]])
            else:
                heapq.heappush(heap, [dist, [x,y]])
            
        return [x[1] for x in heap]

## Min Heap: O(N + k log N) time complexity, O()
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = (x ** 2 + y ** 2)
            
            heap.append([dist, [x, y]])
        
        heapq.heapify(heap)
           
        return [heapq.heappop(heap)[1] for _ in range(k)]

## Quick Select
