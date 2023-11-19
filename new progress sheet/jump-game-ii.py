class Solution:
    def jump(self, nums: List[int]) -> int:

        @cache
        def dp(idx):
            if idx == len(nums)-1:
                return 0
            if idx > len(nums)-1:
                return float('inf')

            tt = float('inf')

            for i in range(idx+1, idx+nums[idx]+1):
                tt = min(tt, dp(i))

            return tt+1

        
        return dp(0)
        