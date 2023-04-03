        
class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Using constant time comp. + O(1) space comp.
        prev = n&1
        while n:
            n = n >> 1
            if n & 1 == prev:
                return False
            prev = n&1
        return True
        