#User function Template for python3

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
            
                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
# } Driver Code Ends