class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        
        total_sum = sum(stones)
        target = math.ceil(total_sum / 2)
        memo = {}

        def dp(i, cur_sum):
            nonlocal total_sum
            if cur_sum > target or i > len(stones)-1:
                return abs(cur_sum - (total_sum - cur_sum))
            
            if (i, cur_sum) in memo:
                return memo[(i, cur_sum)]

            memo[(i, cur_sum)] = min(dp(i+1, cur_sum), dp(i+1, cur_sum+stones[i]))
            return memo[(i, cur_sum)]

        return dp(0, 0)