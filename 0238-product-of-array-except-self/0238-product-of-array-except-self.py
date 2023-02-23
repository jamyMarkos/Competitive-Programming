class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        num_len = len(nums)
        forward = [1]
        backward = [1]
        res = []
        
        
        for i in range(num_len):
            forward.append(forward[-1] * nums[i])
        
        tmp = nums[::-1]
        
        for i in range(num_len):
            backward.append(backward[-1] * tmp[i])
        backward.reverse()
        
        for i in range(num_len):
            res.append(forward[i] * backward[i+1])
            
        return res
            
            
            
        
        
        
            
            
        
            
        