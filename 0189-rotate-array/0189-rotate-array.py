class Solution:
    def invert(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left] 
            left += 1
            right -= 1
        
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        rem = k % len(nums)
        
        self.invert(nums, 0, len(nums) - 1)
        self.invert(nums, 0, rem - 1)
        self.invert(nums, rem, len(nums) - 1)
        
        
            
        
            
        