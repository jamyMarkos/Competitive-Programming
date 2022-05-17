class Solution: 
    def select(self, arr, i):
        return arr[i]
    
    def selectionSort(self, arr,n):
        for i in range(len(arr)):
            min = i
            for j in range(i+1, len(arr)):
                if arr[min] > arr[j]:
                    arr[min], arr[j] = arr[j], arr[min]
            self.select(arr,i)
