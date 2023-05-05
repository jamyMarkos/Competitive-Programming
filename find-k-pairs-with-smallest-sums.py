class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        H = []
        for n in nums1:
            for m in nums2:
                if len(H) < k:
                    heappush(H, (-(n+m), n, m))
                elif H[0] < (-(n+m), n, m):
                    heapreplace(H, (-(m+n), n, m))
                else:
                    break

        return [(n, m) for s, n, m in H]