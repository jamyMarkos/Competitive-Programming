class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = defaultdict(int)

        def dp(cur_sum, idx):
            if cur_sum > target:
                return 0
            elif cur_sum == target:
                return 1
            elif (cur_sum, idx) in memo:
                return memo[(cur_sum, idx)]

            for i in range(len(nums)):
                memo[(cur_sum, idx)] += dp(cur_sum+nums[i], i)

            return memo[(cur_sum, idx)]

        return dp(0, 0)