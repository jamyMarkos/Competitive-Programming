class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        return max(Counter(nums), key=Counter(nums).get)
        

        