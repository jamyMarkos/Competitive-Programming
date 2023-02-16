class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = 0
        odd = 0
        for val in Counter(s).values():
            if val % 2:
                odd = 1
                count += val - 1
            else:
                count += val  
        return count + odd
            
        
        