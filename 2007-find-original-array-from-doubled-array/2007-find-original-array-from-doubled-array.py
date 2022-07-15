class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        Dict = dict()
        ans = []
        changed.sort()
        for i in changed:
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1
        flag = 1
        for i in changed:
            if i != 0:
                if i * 2 in Dict and Dict[i] > 0 and Dict[i * 2] > 0:
                    ans.append(i)
                    Dict[i] -= 1
                    Dict[i * 2] -= 1
            elif flag == 1:
                for i in range(Dict[i] // 2):
                    ans.append(0)
                    flag = 0     
        print(ans)
        if 2 * len(ans) == len(changed) :
            return ans
        else:
            return []

        
                    
            
                
            
                    
            