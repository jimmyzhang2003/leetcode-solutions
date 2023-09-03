# Link: https://leetcode.com/problems/longest-consecutive-sequence/

# Time Complexity: O(N)
# Space Complexity: O(N)
# (Hashset)

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        ans = 0 

        for num in numsSet:
            # find if number is start of sequence
            if num-1 not in numsSet:
                curr = 1
                i = 1

                while num+i in numsSet:
                    curr += 1
                    i += 1
                
                ans = max(curr, ans)
                    
        return ans