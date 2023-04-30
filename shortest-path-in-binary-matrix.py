class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        inbound = lambda x, y: x in range(n) and y in range(n)
        if grid[0][0]:
            return -1
        q = deque([(0,0)])
        lvl = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                if [r, c] == [n-1, n-1]:
                    return lvl
                for dr, dc in directions:
                    nr, nc = dr + r, dc + c
                    if inbound(nr, nc) and not grid[nr][nc]:
                        q.append((nr, nc))
                        grid[nr][nc] = 1
            lvl += 1
        return -1