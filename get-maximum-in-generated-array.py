class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        arr = [0]*(n+1)
        if n > 0:
            arr[1] = 1
        for i in range(2, n+1):
            if not i % 2:
                arr[i] = arr[i//2]
            else:
                arr[i] = arr[i//2] + arr[i//2+1]

        return max(arr)