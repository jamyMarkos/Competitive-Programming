class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        count = 0
        best = 0
        N = len(nums)

        for x in nums:
            best |= x

        def helper(i, cur):
            nonlocal count
            if i == N:
                if cur == best:
                    count += 1
                return
            helper(i+1, cur)
            helper(i+1, cur | nums[i])

        helper(0, 0)
        return count