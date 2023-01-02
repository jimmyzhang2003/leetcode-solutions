# Link: https://leetcode.com/problems/kth-largest-element-in-a-stream/

# Time Complexity: O(N log N) for init, O(log K) for add
# Space Complexity: O(N)
# (Heap)
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.stream = nums
        heapq.heapify(self.stream)
        self.k = k
        
        while len(self.stream) > self.k:
            heapq.heappop(self.stream)

    def add(self, val: int) -> int:
        heapq.heappush(self.stream, val)

        if len(self.stream) > self.k:
            heapq.heappop(self.stream)

        return self.stream[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)