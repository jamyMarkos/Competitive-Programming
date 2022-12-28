class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0
        right = left + 1
        while left < len(nums) and right < len(nums):
            if nums[left] == 0:
                if nums[right] != 0:
                    nums[left], nums[right] = nums[right], nums[left]
                    left += 1
                    right = left + 1
                else:
                    right += 1
            else:
                left += 1
                right = left + 1
                
        return nums


                
