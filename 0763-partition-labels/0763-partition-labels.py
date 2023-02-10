class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        _max = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)):
                if s[j] == s[i]:
                    _max = max(_max, j)
            if _max == i:
                res.append(_max+1)
                _max = i+1
        answer = [res[0]]
        for i in range(1, len(res)):
            answer.append(res[i] - res[i-1])
        return answer
                
        