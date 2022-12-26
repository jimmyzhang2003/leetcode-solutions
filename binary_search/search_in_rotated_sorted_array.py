# Link: https://leetcode.com/problems/search-in-rotated-sorted-array/

# Time Complexity: O(log N)
# Space Complexity: O(1)
# (Binary Search)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid

            # inflection point in left half
            elif nums[l] > nums[mid]:
                # traverse left half if target larger than left or smaller than mid
                if target >= nums[l] or target < nums[mid]:
                    r = mid - 1
                # otherwise traverse right half
                else:
                    l = mid + 1
            # inflection point in right half
            elif nums[r] < nums[mid]:
                # traverse right half if target smaller than right or larger than mid
                if target > nums[mid] or target <= nums[r]:
                    l = mid + 1
                # otherwise traverse left half
                else:
                    r = mid - 1
            # no inflection point
            else:
                # normal binary search
                if nums[mid] > target:
                    r = mid - 1
                elif nums[mid] < target:
                    l = mid + 1
            
        return -1

# Time Complexity: O(log N)
# Space Complexity: O(1)
# (Binary Search Alternative Solution)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # inflection point in right half
            elif nums[mid] >= nums[l]:
                # traverse left half if target in range
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                # otherwise traverse right half
                else:
                    l = mid + 1
            
            # inflection point in left half
            else:
                # traverse right half if target in range
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                # otherwise traverse left half
                else:
                    r = mid - 1
                    
        return -1