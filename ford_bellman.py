
def solve():
    n, m = map(int, input().split())
    edgeList = []
    for _ in range(m):
        a, b, w = map(int, input().split())
        edgeList.append((a-1, b-1, w))
    # Step 1: Initialize distances
    dist = [float('inf')] * n
    dist[0] = 0

    # Step 2: Iterative Relaxation (n-1) times
    for _ in range(n-1):
        for u, v, w in edgeList:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for i in range(n):
        if dist[i] == float('inf'):
            dist[i] = 30000
    print(' '.join(map(str, dist)))


if __name__ == '__main__':
    solve()
