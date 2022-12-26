# Link: https://leetcode.com/problems/coin-change/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Array / Prefix Sum)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forwardProduct = [None for _ in range(len(nums))]
        backwardProduct = [None for _ in range(len(nums))]
        res = []
        
        for i in range(len(nums)):
            if i == 0:
                forwardProduct[i] = nums[i]
            else:
                forwardProduct[i] = nums[i] * forwardProduct[i-1]
                
        for i in range(len(nums)-1, -1, -1):
            if i == len(nums)-1:
                backwardProduct[i] = nums[i]
            else:
                backwardProduct[i] = nums[i] * backwardProduct[i+1]
                
        for i in range(len(nums)):
            if i == 0:
                res.append(backwardProduct[i+1])
            elif i == len(nums)-1:
                res.append(forwardProduct[i-1])
            else:
                res.append(forwardProduct[i-1] * backwardProduct[i+1])
                
        return res

# Time Complexity: O(N)
# Space Complexity: O(1)
# (Array / Prefix Sum (Space-Optimized))
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1 for _ in nums]
        
        l, r = 1, 1
        
        for i in range(len(nums)):
            res[i] *= l
            res[-1 - i] *= r
            l *= nums[i]
            r *= nums[-1 - i]
            
        return res