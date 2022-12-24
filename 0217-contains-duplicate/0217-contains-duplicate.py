class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        if n == 1: return False
        else:
            nums.sort()
            for i in range(1, n):
                if nums[i-1] == nums[i]:
                    return True
            return False