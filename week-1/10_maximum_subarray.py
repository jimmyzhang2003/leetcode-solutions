# Link: https://leetcode.com/problems/maximum-subarray/

# Time Complexity: O(N)
# Space Complexity: O(1)
# (Two Pointers)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        l, r = 0, 1
        largestSum = nums[l] if len(nums) > 0 else None
        prevSum = largestSum
        
        while r < len(nums):
            tmpSum = prevSum + nums[r]
            
            if prevSum < 0 and nums[r] > prevSum:
                prevSum = nums[r]
                largestSum = max(nums[r], largestSum)
                l = r 
            elif tmpSum > largestSum:
                prevSum = tmpSum
                largestSum = tmpSum
            else:
                prevSum = tmpSum
                
            r += 1
        
        return largestSum

# Time Complexity: O(N)
# Space Complexity: O(1)
# Kadane's Algorithm
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = currSum = nums[0]
        
        for x in nums[1:]:
            currSum = max(x+currSum, x)
            maxSum = max(currSum, maxSum)
        
        return maxSum