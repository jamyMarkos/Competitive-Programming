class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        arr = []
        temp = float('inf')
        indexx = -1
        for idx, list_ in enumerate(points):
            if list_[0] == x or list_[1] == y:
                dist = abs(list_[0] - x) + abs(list_[1] - y)
                if dist < temp:
                    temp = dist
                    indexx = idx
                    
        return indexx
                
                
        