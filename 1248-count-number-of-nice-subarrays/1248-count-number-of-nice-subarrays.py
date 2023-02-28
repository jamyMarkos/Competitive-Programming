class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        l = 0
        ans = 0
        sub_count = 0
        odd_count = 0
        
        for r in range(len(nums)):
            if nums[r] % 2:
                odd_count += 1
                sub_count = 0
            
            while odd_count == k:
                if nums[l] % 2:
                    odd_count -= 1
                sub_count += 1
                
                l += 1
            
            ans += sub_count
            
        return ans
    
    