class Solution:
    def sortSentence(self, s: str) -> str:
        arr = s.split(" ")
        arr_2 = [""] * len(arr)
        for i in range(len(arr)):
            p = str(arr[i])[-1]
            arr_2[int(p) - 1] = arr[i][:-1]
            
        newStr = " ".join(arr_2)
        return newStr
        