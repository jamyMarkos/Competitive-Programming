class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        memo = {}
        memo[arr[0]] = 1
        res = 1

        for i in range(1, len(arr)):
            if arr[i] - difference in memo:
                memo[arr[i]] = memo[arr[i]-difference] + 1
                res = max(res, memo[arr[i]])
            else:
                memo[arr[i]] = 1

        return res