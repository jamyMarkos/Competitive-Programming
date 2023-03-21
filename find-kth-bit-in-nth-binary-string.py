class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        
        invert = {"0":"1", "1":"0"}
        
        def helper(n, k): # 0 <= k <= n-1
            mid = 2**(n-1) -1 
            if n == 0:
                return "0"
            elif n == 1:
                return "011"[k]
            elif k == mid:
                return "1"
            elif k < mid:
                return helper(n-1, k)
            else: # k> mid
                return invert[helper(n, 2*mid-k)]
    
        return helper(n, k-1)