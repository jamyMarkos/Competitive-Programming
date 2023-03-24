class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums += [-1]
        i = 0
        while i < len(nums):
            j = nums[i]
            if nums[i] != nums[j] and nums[i] != -1:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1
            
        for i in range(len(nums)):
            if nums[i] == -1:
                return i