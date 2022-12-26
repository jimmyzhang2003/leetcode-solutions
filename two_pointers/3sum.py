# Link: https://leetcode.com/problems/3sum/

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# (Brute Force)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        used = []
        
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                for k in range(j + 1, len(nums)):
                    numsSet = set([nums[i], nums[j], nums[k]])
                    if i != j and i != k and j != k and numsSet not in used and nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
                        used.append(numsSet)
        
        return res

# Time Complexity: O(N^3)
# Space Complexity: O(N^2)
# (Brute Force without Set)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort()
        
        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, len(nums) - 1):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                for k in range(j + 1, len(nums)):
                    if k > j + 1 and nums[k] == nums[k - 1]:
                        continue
                    numsSet = set([nums[i], nums[j], nums[k]])
                    if i != j and i != k and j != k and numsSet and nums[i] + nums[j] + nums[k] == 0:
                        res.append([nums[i], nums[j], nums[k]])
        
        return res

# Time Complexity: O(N^2)
# Space Complexity: O(N^2)
# (Two Pointers)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        
        nums.sort() 
        
        for i in range(0, len(nums) - 2):      
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            l, r = i + 1, len(nums) - 1
            
            while l < r:     
                total = nums[i] + nums[l] + nums[r]
                
                if total < 0:
                    l += 1
                elif total > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                           
        return res