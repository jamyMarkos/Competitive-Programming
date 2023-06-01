class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(cur_sum, i):
            if i == len(nums)-1 and cur_sum == target:
                return 1
            elif i == len(nums)-1 and cur_sum != target:
                return 0
            elif (cur_sum, i) in memo:
                return memo[(cur_sum, i)]

            memo[(cur_sum, i)] = dp(cur_sum+nums[i+1], i+1) + dp(cur_sum-nums[i+1], i+1)

            return memo[(cur_sum, i)]

        return dp(0, -1)