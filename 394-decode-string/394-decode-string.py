class Solution:
    def decodeString(self, s: str) -> str:
        arr = []
        ans = ""
        for i in s:
            if i != "]": arr.append(i)
            else:
                x = ""
                temp = ""
                while arr[-1] != "[":
                    temp = arr.pop() + temp
                arr.pop()
                while len(arr) > 0:
                    if arr[-1] in "[]abcdefghijklmnopqrstuvwxyz": break
                    x = arr.pop() + x
                temp *= int(x)
                for i in temp:
                    arr.append(i)
        for i in arr:
            ans += i
        return ans
                    
                
                
                    
                
                
                    
                    
                
                
                
                
                    
                
                
            
        