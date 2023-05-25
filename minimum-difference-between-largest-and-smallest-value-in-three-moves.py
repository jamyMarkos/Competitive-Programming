class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        posIdx = [(0, -4), (1,-3), (2,-2), (3,-1)]
        
        if len(nums) < 4:
            return 0
        res = float('inf')
        for a, b in posIdx:
            res = min(res, abs(nums[a]-nums[b]))
        return res