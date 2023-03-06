class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        start, end = max(weights), sum(weights)
        # mid_weight = 0
        
        def day_counter(mid):
            sum_ = 0
            day_count = 0
            for i in range(len(weights)):
                sum_ += weights[i]
                if sum_ > mid_weight:
                    day_count += 1
                    sum_ = weights[i]
        
            if sum_ > 0:
                day_count += 1

            return day_count <= days



        while start < end:
            mid_weight = (start + end) // 2

            if day_counter(mid_weight):
                end = mid_weight 
            else:
                start = mid_weight + 1
                
            
        return start