class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        count = 0
        left = right = 0
        while right < len(trainers) and left < len(players):
            if trainers[right] >= players[left]:
                count += 1
                left += 1
            right += 1
        return count
                
        