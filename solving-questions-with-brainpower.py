class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        memo = {}

        def dp(idx):
            if idx > len(q)-1:
                return 0
            if idx in memo:
                return memo[idx]
            memo[idx] = max(dp(idx + q[idx][1] + 1) + q[idx][0], dp(idx + 1))
            return memo[idx]

        return dp(0)