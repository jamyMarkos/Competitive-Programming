class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        dict_ = {}
        
        for word in words:
            uniqL = Counter(word)
            temp = ''.join(sorted(uniqL.keys()))
            if temp in dict_:
                count += dict_[temp]
                dict_[temp] += 1
            else:
                dict_[temp] = 1
                
        return count
            
            
        