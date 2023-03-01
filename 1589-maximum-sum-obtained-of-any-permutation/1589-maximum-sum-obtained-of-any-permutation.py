class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        preSum = [0] * (len(nums) + 1)
        
        const = 10 ** 9 + 7
        
        for request in requests:
            preSum[request[0]] += 1
            preSum[request[1] + 1] -= 1
            
        preSum = list(accumulate(preSum[:-1]))
        
        preSum.sort()
        nums.sort()
        
        res = 0
        
        for i in range(len(nums)):
            res += (nums[i] * preSum[i])
            
        return res % const
            
        