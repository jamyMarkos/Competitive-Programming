class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        arr = [0] * (len(s) + 1)
        
        for shift in shifts:
            if not shift[2]:
                arr[shift[0]] -= 1
                arr[shift[1] + 1] += 1
            else:
                arr[shift[0]] += 1
                arr[shift[1] + 1] -= 1
        
        arr = list(accumulate(arr))[:len(s)]
        
        for i in range(len(s)):
            arr[i] += ord(s[i])
            arr[i] = (arr[i] - ord('a')) % 26
      
        return ''.join([chr(97+num) for num in arr])
            
         
        
            
        
        
        
        
        
        