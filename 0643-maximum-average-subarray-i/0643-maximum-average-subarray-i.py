class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window = nums[:k]
        tmp = sum(window)
        max_ = tmp
 
        for i in range(k, len(nums)):
            startInd = i - k
            tmp = tmp - nums[startInd] + nums[i]
            max_ = max(tmp, max_)
            
            
        return max_ / k
            
        
            
        