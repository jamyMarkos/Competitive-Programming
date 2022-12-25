class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        r1 = r2 = 0
        num1, num2 = num1[-1::-1], num2[-1::-1]
        for i, dgt1 in enumerate(num1):
            r1 += int(dgt1) * (10**i)
              
        for j, dgt2 in enumerate(num2):
            r2 += int(dgt2) * (10**j)
        
        return str(r1 * r2)
        
        
     
            
        
        
        