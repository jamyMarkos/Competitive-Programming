class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        defdict = defaultdict(int)
        for i in range(len(s)):
            if s[i] not in defdict:
                defdict[s[i]] += 1
            else:
                break
        max_ = len(defdict.keys())
        if max_ == len(s):
            return max_
        left, right = 0, i
        
        while right < len(s):
            if defdict[s[right]] < 1:
                defdict[s[right]] += 1
                right += 1
                max_ = max(max_, right - left)
            else:
                
                while left < right and defdict[s[right]] != 0 :
                    defdict[s[left]] -= 1
                    left += 1
           
        return max_
            
        