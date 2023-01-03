class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        m = 10**9 + 7
        d = defaultdict(int)
        ans = 0
        for i in deliciousness:
            for j in range(22):
                k = 2**j - i
                if k in d:
                    ans += d[k]
            d[i] += 1
        return ans % m
            
        