class Solution:
    def freqAlphabets(self, s: str) -> str:
        llist = []
        sstr = "abcdefghijklmnopqrstuvwxyz"
        for i in range(26):
            llist.append(i+1)
        dict_ = dict(zip(llist, sstr))
        
        right, ans = len(s) - 1, ''
        while right >= 0:
            if s[right] != '#':
                ans = dict_[int(s[right])] + ans
                right -= 1
            else:
                temp = int(s[right-2:right])
                ans = dict_[temp] + ans
                right -= 3
        
        return ans
                
                
                
            
        
        
        
        
        
        
        

            
        
                
            
           