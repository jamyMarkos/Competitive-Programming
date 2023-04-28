class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n, path_len = len(grid), float('inf')
        
        # if n == 1:return 1
        if grid[0][0]:
            return -1
        q = deque()
        q.append((0, 0, 1))
        
        directions = [(1,0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, -1), (-1, 1)]
        
        inbound = lambda x, y: 0 <= x < n and 0 <= y < n
        
        def bfs():
            nonlocal path_len
            while q:
                for i in range(len(q)):
                    x, y, dist = q.popleft()
                    if [x, y] == [n-1, n-1]:
                        path_len = min(path_len, dist)
                        
                    for dx, dy in directions:
                        newX, newY = x + dx, y + dy
                        
                        if not inbound(newX, newY) or grid[newX][newY] == 1:
                            continue
                        elif inbound(newX, newY) and not grid[newX][newY]:
                            q.append((newX, newY, dist+1))
                            grid[newX][newY] = 1
      
        bfs()
        return -1 if path_len == float('inf') else path_len
        