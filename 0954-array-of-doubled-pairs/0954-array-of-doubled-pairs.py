class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        dict_ = Counter(arr)
        arr.sort(key=abs)
        print(arr)
        for el in arr:
            doubled = 2 * el
            if doubled in dict_ and dict_[el] > 0 and dict_[doubled] > 0:
                dict_[el] -= 1
                dict_[doubled] -= 1
            elif dict_[el] > 0:
                if (doubled in dict_ and dict_[doubled] == 0) or doubled not in dict_:
                    return False
        return True
                
                    
                
                
                    
            
                