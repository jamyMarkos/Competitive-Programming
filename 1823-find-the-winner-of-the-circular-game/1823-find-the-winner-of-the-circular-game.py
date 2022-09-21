class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = [i+1 for i in range(n)]
        while len(queue) != 1:
            for i in range(k-1):
                queue.append(queue.pop(0))
            queue.pop(0)
        return queue[0]
        