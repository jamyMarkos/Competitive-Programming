class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        slow, fast = 1, max(piles)
        speed = 0

        if len(piles) == 1:
            return math.ceil(piles[0] / h)

        
        while slow <= fast:
            speed = (slow + fast) // 2
            hours_spend = 0

            for num in piles:
                hours_spend += math.ceil(num / speed)
            
            if hours_spend <= h:
                fast = speed - 1
                
            elif hours_spend > h:
                slow = speed + 1
            
        return slow