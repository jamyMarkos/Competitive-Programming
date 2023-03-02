class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        front, rear = 0, len(tickets) - 1

        time = 0

        while tickets[k] != 0:
            if tickets[front]:
                tickets[front] -= 1
                time += 1
                
            rear = (rear + 1) % len(tickets)
            front = (front + 1) % len(tickets)
        
        return time