# Link: https://leetcode.com/problems/k-closest-points-to-origin/

# Time Complexity: O(N log K)
# Space Complexity: O(K)
# (Max Heap)
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


# Time Complexity: O(N + k log N)
# Space Complexity: O(N)
# (Min Heap)
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            dist = (x ** 2 + y ** 2)
            
            heap.append([dist, [x, y]])
        
        heapq.heapify(heap)
           
        return [heapq.heappop(heap)[1] for _ in range(k)]

# Time Complexity: O(N) average case and O(N^2) worst case
# Space Complexity: O(1)
# (Quickselect)
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def dist(point):
            return point[0] ** 2 + point[1] ** 2
        
        def partition(points, l, r):
            #pick a random element to be the pivot
            pivot = random.randint(l, r)
            
            #swap pivot to the end
            points[r], points[pivot] = points[pivot], points[r]
            
            ptr = l
            
            for i in range(l, r):
                if dist(points[i]) <= dist(points[r]):
                    points[ptr], points[i] = points[i], points[ptr]
                    ptr += 1
            
            #swap pivot back
            points[ptr], points[r] = points[r], points[ptr]
            
            return ptr
    
        l, r = 0, len(points) - 1

        while l < r:
            mid = partition(points, l, r)
            
            if mid < k:
                l = mid + 1
            elif mid > k:
                r = mid - 1
            else:
                break
            
        return points[:k]

