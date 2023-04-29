class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(mat), len(mat[0])
        inbound = lambda x, y: x in range(n) and y in range(m)
        q = deque()
        visit = set()
        ans = [[0] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                if not mat[i][j]:
                    q.append((i, j))
                    visit.add((i, j))
                    
        lvl = 1
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                for dx, dy in directions:
                    nr, nc = dx + r, dy + c

                    if inbound(nr, nc) and (nr, nc) not in visit and mat[nr][nc]:
                        ans[nr][nc] = lvl
                        q.append((nr, nc))
                        visit.add((nr, nc))

            lvl += 1

        return ans