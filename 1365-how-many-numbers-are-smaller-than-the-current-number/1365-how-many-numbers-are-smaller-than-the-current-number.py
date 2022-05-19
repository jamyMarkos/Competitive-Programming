class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = sorted(nums)
        cnt = []
        for i in range(len(nums)):
            curr = arr.index(nums[i])
            cnt.append(curr)
        return cnt
        
            
       
            
            
            
            
            
            