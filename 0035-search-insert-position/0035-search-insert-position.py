class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        
        low, high = 0, len(nums) - 1
        
        mid = (high + low) // 2
        
        while high > low:
            if target > nums[mid]:
                low = mid + 1
            elif target < nums[mid]:
                high = mid 
            else:
                return mid
                
            mid = (high + low) // 2
        if mid < 0:
            return 0
      
        return mid if target <= nums[low] else mid + 1
            