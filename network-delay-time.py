class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, source: int) -> int:
        dist = [[float('inf')] * n for _ in range(n)]
        
        for u, v, w in times:
            dist[u-1][v-1] = w

        for i in range(n):
            dist[i][i] = 0

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

        tt = max(dist[source-1])
        return tt if tt != float('inf') else -1