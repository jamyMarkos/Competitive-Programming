class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        defdict = defaultdict(int)
        nums += list(map(int, [str(x)[::-1].lstrip('0') for x in nums]))
        for el in nums:
            defdict[el] += 1
        return len(defdict.keys())
        
            
            
            
        
        