# Link: https://leetcode.com/problems/kth-largest-element-in-an-array/

# Time Complexity: O(N log K)
# Space Complexity: O(N)
# (Min Heap)
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        for _ in range(len(nums)-k):
            heapq.heappop(nums)

        return heapq.heappop(nums)