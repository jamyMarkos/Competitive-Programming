class Solution:
    def numTeams(self, rating: List[int]) -> int:
        def helper(rating):
            N = len(rating)
            pos_hash = {rating[i]: i for i in range(N)}
            rating.sort()

            ans = 0
        
            memo = {}

            def dp(idx, team_count):
                nonlocal N
                if idx > N-1:
                    return 0

                if team_count == 3:
                    return 1

                if (idx, team_count) in memo:
                    return memo[(idx, team_count)]


                value = 0

                for j in range(idx+1, N):
                    if pos_hash[rating[j]] > pos_hash[rating[idx]]:
                        value += dp(j, team_count+1)

                memo[(idx, team_count)] = value

                return memo[(idx, team_count)]
                
            for i in range(N):
                ans += dp(i, 1)

            return ans

        
        return helper(rating[::-1]) + helper(rating)