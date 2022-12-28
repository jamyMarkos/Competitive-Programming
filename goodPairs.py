class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        dict_ = {}
        counter = 0
        
        for num in nums:
            
            if num in dict_:
                counter += dict_[num]
                dict_[num] += 1
            else:
                dict_[num] = 1
                
        return counter
        
            
        
        
        
        
