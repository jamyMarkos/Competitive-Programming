class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        ans = [-1] * n
        stack = []
       
        for i in list(range(n)) * 2:
            while stack and nums[stack[-1]] < nums[i]:
                ans[stack.pop()] = nums[i]
            stack.append(i)

        return ans