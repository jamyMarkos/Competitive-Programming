class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        temp = 0
        for i in range(len(s)):
            if temp < len(spaces) and spaces[temp] == i:
                res.append(' ')
                res.append(s[i])
                temp += 1
            else:
                res.append(s[i])
        return ''.join(res)

            
                
            
        
        