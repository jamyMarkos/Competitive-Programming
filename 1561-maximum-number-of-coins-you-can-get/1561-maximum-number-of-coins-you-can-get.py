class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        j = 0
        sum = 0
        for i in range(1, len(piles), 2):
            if j < len(piles) // 3:
                sum += piles[-(i+1)]
                j += 1
        return sum
            
        
        