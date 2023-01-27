class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0
        left, right = 0, len(nums) - 1
        while left < right:
            temp = nums[left] + nums[right]
            if temp > k:
                right -= 1
            elif temp < k:
                left += 1
            
            else:
                count += 1
                left += 1
                right -= 1
                
        return count
                
            
        