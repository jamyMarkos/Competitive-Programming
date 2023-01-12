class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        left, right = 0, 1
        while right < len(nums):
            if nums[right] == nums[left]:
                nums[left], nums[right] = 2 * nums[left], 0
            left += 1
            right = left + 1
        print(nums)
        i = 0
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        return nums
            
                
                
            
                
            
        