class Solution:
    def printVertically(self, s: str) -> List[str]:
        temp = s.split()
        list_ = sorted(temp, key=len)
        arr = []
        for i in range(len(list_[-1])):
            ans = []
            for word in temp:
                if i >= len(word):
                    ans.append(' ')
                else:
                    ans.append(word[i])
                
            arr.append(''.join(ans).rstrip())
            
        return arr
                
                
            
        
        