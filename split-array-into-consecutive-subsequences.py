class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        ans = []
        for num in nums:
            flag = False
            for i in reversed(range(len(ans))):
                if not ans:
                    ans.append([num])
                if num - ans[i][-1] == 1:
                    ans[i].append(num)
                    flag = True
                    break
            if not flag:
                ans.append([num])

        return all(len(x) >= 3 for x in ans)