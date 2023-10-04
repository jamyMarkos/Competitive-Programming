class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                
                if i == m-1 and j != n-1:
                    dungeon[i][j] += dungeon[i][j+1]
                elif j == n-1 and i != m-1:
                    dungeon[i][j] += dungeon[i+1][j]
                
                elif i != m-1 and j != n-1:
                    dungeon[i][j] += max(dungeon[i+1][j], dungeon[i][j+1])
                
                dungeon[i][j] = min(0, dungeon[i][j])
        
        return abs(dungeon[0][0])+1