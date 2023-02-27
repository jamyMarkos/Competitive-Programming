class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        preSum = [nums[0]]
        for num in nums[1:]:
            preSum.append(preSum[-1] + num)    
        return preSum