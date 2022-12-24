class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        hash_ = Counter(arr)
        for i in arr:
            if i == 0 and hash_[i] > 1:
                return True
                
            elif i != 0 and hash_[i*2]:
                return True
            
        return False
        
        