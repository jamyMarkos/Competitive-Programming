class Solution:
    def sortColors(self, nums: List[int]) -> None:
        # count = [0] * 3
        # for color in nums:
        #     count[color] += 1
        # track = 0
        # for i in range(len(count)):
        #     for j in range(count[i]):
        #         if track < len(nums):
        #             nums[track] = i
        #         track += 1
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
            
            
        

       
            
            
        
        
       
        