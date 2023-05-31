class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def dp(idx, _len, memo):

            if idx >= _len:
                return 0
            if idx in memo:
                return memo[idx]
            
            memo[idx] = max(nums[idx] + dp(idx+2, _len, memo), dp(idx+1, _len, memo))
            return memo[idx]
        
        return max(dp(0, len(nums)-1, {}), dp(1, len(nums), {}))