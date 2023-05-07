class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        inbound = lambda x, y: x in range(n) and y in range(n)
        q = deque()

        def dfs(x, y):
            visit[x][y] = True
            for dr, dc in directions:
                nr = dr + x
                nc = dc + y
                if inbound(nr, nc) and not visit[nr][nc] and grid[nr][nc]:
                    q.append((nr, nc))
                    dfs(nr, nc)

        visit = [[False] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if grid[i][j]:
                    q.append((i, j))
                    visit[i][j] = True
                    dfs(i, j)
                    break
            else:
                continue
            break


        short_bridge = 0
        def bfs():
            nonlocal short_bridge 
            while q:
                for _ in range(len(q)):
                    x, y = q.popleft()
                    for dr, dc in directions:
                        nr = dr + x
                        nc = dc + y
                        if inbound(nr, nc) and not visit[nr][nc]:
                            q.append((nr, nc))
                            visit[nr][nc] = True
                            if grid[nr][nc]:
                                return short_bridge
                short_bridge += 1

        return bfs()