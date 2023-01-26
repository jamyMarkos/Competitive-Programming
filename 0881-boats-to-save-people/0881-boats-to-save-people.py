class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        num_boats = 0
        left, right = 0, len(people) - 1
        while left <= right:
            if people[right] + people[left] > limit:
                right -= 1
            else:
                left += 1
                right -= 1
            num_boats += 1    
        
        return num_boats
                
            
        