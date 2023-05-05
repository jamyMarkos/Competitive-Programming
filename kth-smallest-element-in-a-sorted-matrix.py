class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        H = []
        n = len(matrix)
        for r in range(n):
            for c in range(n):
                tt = -matrix[r][c]
                if len(H) < k:
                    heappush(H, tt)
                elif H[0] < -matrix[r][c]:
                    heapreplace(H, tt)
                
        return -H[0]