class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = defaultdict(int)
        

        def recur(step):
            if step >= len(cost):
                return 0
            if step in memo:
                return memo[step]
            memo[step] = min(recur(step+1), recur(step+2)) + cost[step]

            return memo[step] 
        
        return min(recur(0), recur(1))