class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        n, m = len(maze), len(maze[0])
        
        q = deque([(entrance[0], entrance[1])])
        inbound = lambda x, y: x in range(n) and y in range(m)
        lvl = 0
        while q:
            for i in range(len(q)):
                row, col = q.popleft()
                
                if [row, col] != entrance:
                    for dx, dy in directions:
                        if not inbound(row+dx, col+dy):
                            return lvl
                
                for dx, dy in directions:
                    new_row = dx + row
                    new_col = dy + col
                    
                    if not inbound(new_row, new_col) or maze[new_row][new_col] == '+':
                        continue
                    
                    elif inbound(new_row, new_col):
                        q.append((new_row, new_col))
                        maze[new_row][new_col] = '+'
            lvl += 1
                        
                    
                    
        return -1
        