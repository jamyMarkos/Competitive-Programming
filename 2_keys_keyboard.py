class Solution:
    def minSteps(self, n: int) -> int:
        res = 1
        tt = 0
        copy = 0

        while res < n:
            if not n % res:
                copy = res 
                tt += 1
            res += copy
            tt += 1
         
        return tt