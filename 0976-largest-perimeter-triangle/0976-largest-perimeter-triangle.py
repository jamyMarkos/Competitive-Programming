class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        max_ = 0
        left, right = n - 3, n
        while left >= 0:
            temp = nums[left : right]
            
            if temp[2] < sum(temp[:-1]):
                return sum(temp)
            left, right = left - 1, right - 1
        
        return 0
        
        
        
        