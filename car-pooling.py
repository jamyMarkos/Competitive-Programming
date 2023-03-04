class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: x[2])
        preSum = [0] * (trips[-1][2] + 1)
        print(preSum)
        
        for num, start, end in trips:
            preSum[start] += num
            preSum[end] -= num

        preSum.pop()

        preSum = list(accumulate(preSum))

        return max(preSum) <= capacity