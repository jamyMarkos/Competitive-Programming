class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            _max = i
            for j in range(i, len(nums)):
                if str(nums[_max]) + str(nums[j]) < str(nums[j]) + str(nums[_max]):
                    _max = j
            nums[i], nums[_max] = nums[_max], nums[i]
        
        ans = ''.join(map(str,nums))  
        if ans[0] == '0':
            return '0'
        return ans
        
                            
                
                
        
        
        
        
                
                
        
        
        