class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        
        def gcf(a, b):
            if not b:
                return a
            return gcf(b, a % b)
        
        return gcf(min_, max_)