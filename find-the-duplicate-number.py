class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Using cyclic sort
        i = 0
        while i < len(nums):
            j = nums[i] - 1
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            elif nums[i] == nums[j] and i == j:
                i += 1
            else:
                return nums[i]
            
        # return nums[-1]