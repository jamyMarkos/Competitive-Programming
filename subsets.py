class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ans = [[]]
        
        def backtrack(arr, idx):
            if len(arr) == n:
                return 
            for j in range(idx+1, n):
                ans.append(arr + [nums[j]])
                backtrack(arr + [nums[j]], j)

        for i in range(n):
            ans.append([nums[i]])
            backtrack([nums[i]], i)

        return ans