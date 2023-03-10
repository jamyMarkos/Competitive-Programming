class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = []
        def backtrack(cur, path):
            if len(path) == k:
                answer.append(path)
                return
            for i in range(cur+1, n+1):
                backtrack(i, path + [i])
        for i in range(1, n+1):
            backtrack(i, [i])
        return answer