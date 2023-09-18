class Solution:
    def minSteps(self, n: int) -> int:
    
        clipboard = 1
        res = 1
        count = 0

        while res < n:
            res += clipboard
            if n % res == 0:
                clipboard = res
                count += 1
            count += 1

        return count



        
