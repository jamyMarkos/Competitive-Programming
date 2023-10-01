class Solution:
    def longestPalindromeSubseq(self, s1: str) -> int:
        s2 = s1[::-1]
        memo = {}
        def dp(i1, i2):
            if i1 >= len(s1) or i2 >= len(s2):
                return 0
            if (i1, i2) in memo:
                return memo[(i1, i2)]
            
            if s1[i1] == s2[i2]:
                memo[(i1, i2)] = dp(i1+1, i2+1) + 1
            else:
                memo[(i1, i2)] = max(dp(i1+1, i2), dp(i1, i2+1))
            return memo[(i1, i2)]

        return dp(0, 0)