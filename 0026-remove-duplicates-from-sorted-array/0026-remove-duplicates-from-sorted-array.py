class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        for j in range(len(nums)):
            if i == 0:
                i += 1
            elif nums[j] > nums[i-1]:
                nums[i] = nums[j]
                i += 1
        return i 
                
        