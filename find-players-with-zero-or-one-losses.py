class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        hash_won = Counter([win for win, loss in matches])
        hash_lost = Counter([loss for win, loss in matches])

        ans = [[],[]]

        for player in hash_won:
            if player not in hash_lost:
                ans[0].append(player)
            if hash_lost[player] == 1:
                ans[1].append(player)
                
        for player in hash_lost:
            if player not in hash_won and hash_lost[player] == 1:
                ans[1].append(player)

        return [sorted(ans[0]), sorted(ans[1])]