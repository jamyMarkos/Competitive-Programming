class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        left = float('inf')
        mid = float('inf')

        for i in range(len(nums)):
            if nums[i] > mid:
                return True
            elif left < nums[i] < mid:
                mid = nums[i]
            elif nums[i] < left:
                left = nums[i]
                
        return False