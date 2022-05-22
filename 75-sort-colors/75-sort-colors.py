class Solution:
    def sortColors(self, nums: List[int]) -> None:
        count = [0] * 3
        for i in range(len(nums)):
            count[nums[i]] += 1
        for i in range(1,len(count)):
            count[i] += count[i-1]
        temp = [0] * len(nums)
        for i in range(len(nums)):
            count[nums[i]] -= 1
            temp[count[nums[i]]] = nums[i]
        for i in range(len(nums)):
            nums[i] = temp[i]
            
            
        

       
            
            
        
        
       
        