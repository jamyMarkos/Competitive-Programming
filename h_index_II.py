
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        
        def isPossible(n):
            cnt = 0
            for num in citations:
                if num >= n:
                    cnt += 1
            return cnt >= n

        l, r = -1, max(citations) + 1
        while l+1 < r:
            mid = (l + r)//2
            if isPossible(mid):
                l = mid
            else:
                r = mid
        return l