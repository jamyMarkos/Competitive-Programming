class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Dict = defaultdict(int)
        l = 0
        res = 0
      
        for r in range(len(s)):
            Dict[s[r]] += 1
            while Dict[s[r]] > 1:
                Dict[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
                    
        return res
                    
        