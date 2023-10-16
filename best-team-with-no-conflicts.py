class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        N = len(scores)
        pairs = sorted([[scores[i], ages[i]] for i in range(N)])
        dp = [pairs[i][0] for i in range(N)]

        for i in range(N):
            mScore, mAge = pairs[i]
            for j in range(i):
                score, age = pairs[j]
                if mAge >= age:
                    dp[i] = max(dp[i], mScore + dp[j])
                
        return max(dp)