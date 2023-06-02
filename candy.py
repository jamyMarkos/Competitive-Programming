class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        l_r, r_l = [1]*n, [1]*n
        tt = 0
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                l_r[i] = l_r[i-1]+1
        
        for i in range(1, n)[::-1]:
            if ratings[i-1] > ratings[i]:
                r_l[i-1] = r_l[i]+1

        for i in range(n):
            tt += max(l_r[i], r_l[i])

        return tt