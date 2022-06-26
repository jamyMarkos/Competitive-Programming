class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        Dic = dict()
        count = 0
        for i in nums:
            if i in Dic:
                count += Dic[i]
                Dic[i] += 1
            else:
                Dic[i] = 1
        return count
            
        
            
        
        
        
        