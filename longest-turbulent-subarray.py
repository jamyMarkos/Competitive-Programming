class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        max_len = 1
        arr_len = len(arr)
        l = 0
        r = 1
        tmp = sorted(arr)
        if tmp[-1] == tmp[0]:
            return 1
        flag = False
        while r < arr_len - 1:
            flag = True
            if (arr[r-1] < arr[r] > arr[r+1]) or (arr[r-1] > arr[r] < arr[r+1]):
                r += 1
                continue

            else:
                max_len = max(max_len, r - l + 1)
                while r < arr_len - 1 and arr[r] == arr[r+1]:
                    r += 1
                l = r
            r += 1
        else:
            if flag:
                max_len = max(max_len, r - l + 1)
            elif arr_len == 2 and arr[-1] != arr[0]:
                return 2

        return max_len