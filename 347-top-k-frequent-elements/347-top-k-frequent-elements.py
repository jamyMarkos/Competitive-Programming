class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        Dict = dict()
        ans = []
        for i in nums:
            if i in Dict:
                Dict[i] += 1
            else:
                Dict[i] = 1
        Dict = sorted(Dict.items(), key = lambda x: x[1], reverse=True)
        count = 0
        for i in Dict:
            if k > count:
                ans.append(i[0])
            count += 1
        return ans
            
            
        