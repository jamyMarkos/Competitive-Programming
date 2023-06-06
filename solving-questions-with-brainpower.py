class Solution:
    def mostPoints(self, q: List[List[int]]) -> int:
        memo = {}

        def dp(idx):
            if idx > len(q)-1:
                return 0
            if idx in memo:
                return memo[idx]

            solved = dp(idx + q[idx][1] + 1)
            not_solved = dp(idx + 1)
            memo[idx] = max(solved + q[idx][0], not_solved)
            return memo[idx]

        return dp(0)