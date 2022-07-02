class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        _list = []
        for i in range(1, len(nums) // 2 + 1 ):
            _list.append(nums[i-1] + nums[-i])
        return max(_list)
            
            
            
        