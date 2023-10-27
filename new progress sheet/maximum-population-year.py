class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        
        start = 1950
        end = 2050

        ans = [0, 0]
        for year in range(start, end+1):
        
            tt = [year, 0]
            
            for birth, death in logs:
                if birth <= year < death:
                    tt[1] += 1

            if tt[1] > ans[1]:
                ans[0], ans[1] = tt[0], tt[1]

        
        return ans[0]
