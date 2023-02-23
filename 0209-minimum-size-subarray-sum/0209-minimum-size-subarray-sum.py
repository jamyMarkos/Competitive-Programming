class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_len = float('inf')
        left, right = 0, 0
        sum_ = 0
      
        while right < len(nums):
            if sum_ >= target:
                min_len = min(min_len, right - left)
                sum_ -= nums[left]
                left += 1
                    
            elif sum_ < target:
                sum_ += nums[right]
                right += 1
        while sum_ >= target:
            min_len = min(min_len, right - left)
            sum_ -= nums[left]
            left += 1
            
        if min_len == float('inf'):
            return 0
        return min_len
            
            
            
        