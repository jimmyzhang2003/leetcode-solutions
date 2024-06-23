# Link: https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Monotonic Queue, Sliding Window)
from collections import deque

class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        maxLength = 1
        l = 0

        maxQ = deque() # monotonically decreasing queue
        minQ = deque() # monotonically increasing queue
        maxQ.append(nums[0])
        minQ.append(nums[0])

        for r in range(1, len(nums)):
            while maxQ and nums[r] > maxQ[-1]:
                maxQ.pop()
            maxQ.append(nums[r])

            while minQ and nums[r] < minQ[-1]:
                minQ.pop()
            minQ.append(nums[r])

            while l < r and maxQ[0] - minQ[0] > limit:
                if nums[l] == maxQ[0]:
                    maxQ.popleft()
                
                if nums[l] == minQ[0]:
                    minQ.popleft()

                l += 1
                
            maxLength = max(maxLength, r-l+1)

        return maxLength