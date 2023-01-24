class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        for i in range(len(nums)):
            for j in range(len(nums) - 1):
                if int(nums[j] + nums[j+1]) > int(nums[j+1] + nums[j]):
                    continue
                else:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        ans = ''.join(nums)
        # remove the leading zeros
        return (ans if int(ans) != 0 else '0')
        
        