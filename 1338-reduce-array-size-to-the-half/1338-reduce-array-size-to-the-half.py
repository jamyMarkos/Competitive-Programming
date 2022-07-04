class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        Dict = dict()
        for i in arr:
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1
        Dict = sorted(Dict.items(), key=lambda x: x[1],reverse=True)
        temp = 0
        sum = 0
        for i in Dict:
            sum += i[1]
            if sum >= len(arr) // 2:
                return temp + 1
            else:
                temp += 1
        return temp
    
        