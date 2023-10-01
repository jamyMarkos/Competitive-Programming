class Solution:
    def maxSatisfaction(self, s: List[int]) -> int:
        s.sort()
        sum_ = sum(s)
        max_,n = 0, len(s)
        t = 1
        for i in range(n):
            max_ += (s[i] * t)
            t += 1
        
        max_co = max_
        for i in range(n):
            sum_ -= s[i]
            max_ = max_ - s[i] - sum_
            max_co = max(max_co, max_)
            
        return max_co